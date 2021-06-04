from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from adminapp.forms import ShopUserAdminEditForm, ProductCategoryEditForm, ProductEditForm
from authapp.forms import ShopUserRegisterForm, ShopUserEditForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


class SuperUserOnlyMixin:
    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PageTitleMixin:
    page_title_key = 'title'
    title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.page_title_key] = self.title
        return context


class UserCreateViews(SuperUserOnlyMixin, PageTitleMixin, CreateView):
    model = ShopUser
    title = 'пользователи/создание'
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin:users')
    form_class = ShopUserRegisterForm

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'пользователи/создание'
    #     return context


# @user_passes_test(lambda user: user.is_superuser)
# def user_create(request):
#     title = 'пользователи/создание'
#
#     if request.method == 'POST':
#         user_form = ShopUserRegisterForm(request.POST, request.FILES)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('admin:users'))
#     else:
#         user_form = ShopUserRegisterForm()
#
#     content = {
#         'title': title,
#         'update_form': user_form
#     }
#
#     return render(request, 'adminapp/user_update.html', content)


class UsersListViews(SuperUserOnlyMixin, PageTitleMixin, ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'
    title = 'админка/пользователи'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(object_list=object_list, **kwargs)
    #     context['title'] = 'админка/пользователи'
    #     return context

    # чтобы вывести, к примеру, только "активных пользователей", то нужно переопределить queryset таким образом:
    # def get_queryset(self):
    #     return super().get_queryset().filter(is_active=True)

    # для ордеринка(для упорядочивания) есть метод, его тоже надо переопределить:
    # def get_ordering(self):
    #     return super().queryset.order_by('-name')


# @user_passes_test(lambda user: user.is_superuser)
# def users(request):
#     title = 'админка/пользователи'
#
#     users_list = ShopUser.objects.all()
#
#     content = {
#         'title': title,
#         'objects': users_list
#     }
#
#     return render(request, 'adminapp/users.html', content)

class UserUpdateViews(SuperUserOnlyMixin, PageTitleMixin, UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin:user_update')
    form_class = ShopUserAdminEditForm
    title = 'пользователи/редактирование'

    # form_class = ShopUserEditForm

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'пользователи/редактирование'
    #     return context


# @user_passes_test(lambda user: user.is_superuser)
# def user_update(request, pk):
#     title = 'пользователи/редактирование'
#
#     edit_user = get_object_or_404(ShopUser, pk=pk)
#     if request.method == 'POST':
#         user_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('admin:user_update', args=[edit_user.pk]))
#     else:
#         user_form = ShopUserAdminEditForm(instance=edit_user)
#
#     content = {
#         'title': title,
#         'update_form': user_form,
#     }
#     return render(request, 'adminapp/user_update.html', content)

class UserDeleteViews(SuperUserOnlyMixin, PageTitleMixin, DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('admin:users')
    title = 'пользователи/удаление'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'пользователи/удаление'
    #     return context


# @user_passes_test(lambda user: user.is_superuser)
# def user_delete(request, pk):
#     title = 'пользователи/удаление'
#
#     user = get_object_or_404(ShopUser, pk=pk)
#     if request.method == 'POST':
#         # edit_user.delete()
#         user.is_active = False
#         user.save()
#         return HttpResponseRedirect(reverse('admin:users'))
#
#     content = {
#         'title': title,
#         'user_to_delete': user,
#     }
#     return render(request, 'adminapp/user_delete.html', content)


class ProductCategoryCreateView(SuperUserOnlyMixin, PageTitleMixin, CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin:categories')
    # page_title = 'категории/создание'
    # fields = '__all__'
    #   либо можно поставить форму вместо "fields", это взаимоисключающие вещи
    form_class = ProductCategoryEditForm
    title = 'категории/создание'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'категории/создание'
    #     return context


# @user_passes_test(lambda user: user.is_superuser)
# def category_create(request):
#     title = 'категории/создание'
#
#     if request.method == 'POST':
#         category_form = ProductCategoryEditForm(request.POST, request.FILES)
#         if category_form.is_valid():
#             category_form.save()
#             return HttpResponseRedirect(reverse('admin:categories'))
#     else:
#         category_form = ProductCategoryEditForm()
#
#     content = {
#         'title': title,
#         'update_form': category_form,
#     }
#     return render(request, 'adminapp/category_update.html', content)

class ProductCategoriesListView(SuperUserOnlyMixin, PageTitleMixin, ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'
    title = 'админка/категории'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(object_list=object_list, **kwargs)
    #     context['title'] = 'админка/категории'
    #     return context


# @user_passes_test(lambda user: user.is_superuser)
# def categories(request):
#     title = 'админка/категории'
#
#     categories_list = ProductCategory.objects.all()
#
#     content = {
#         'title': title,
#         'objects': categories_list,
#     }
#
#     return render(request, 'adminapp/categories.html', content)


class ProductCategoryUpdateView(SuperUserOnlyMixin, PageTitleMixin, UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin:category_update')
    # fields = '__all__'
    form_class = ProductCategoryEditForm
    title = 'категории/редактирование'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'категории/редактирование'
    #     return context


# @user_passes_test(lambda user: user.is_superuser)
# def category_update(request, pk):
#     title = 'категории/редактирование'
#
#     category = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         category_form = ProductCategoryEditForm(request.POST, request.FILES, instance=category)
#         if category_form.is_valid():
#             category_form.save()
#             return HttpResponseRedirect(reverse('admin:category_update', args=[category.pk]))
#     else:
#         category_form = ProductCategoryEditForm(instance=category)
#
#     content = {
#         'title': title,
#         'update_form': category_form,
#     }
#     return render(request, 'adminapp/category_update.html', content)


class ProductCategoryDeleteView(SuperUserOnlyMixin, PageTitleMixin, DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('admin:categories')
    title = 'категории/удаление'

    # Вроде как вот то, что ниже в этом классе не нужно, а то приводит к ошибкам..почему - не ведаю пока что

    # @method_decorator(user_passes_test(lambda user: user.is_superuser))
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)
    #
    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     context_data['title'] = 'категории/удаление'
    #     return context_data

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


# @user_passes_test(lambda user: user.is_superuser)
# def category_delete(request, pk):
#     title = 'категории/удаление'
#
#     category = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         # edit_user.delete()
#         category.is_active = False
#         category.save()
#         return HttpResponseRedirect(reverse('admin:categories'))
#
#     content = {
#         'title': title,
#         'category_to_delete': category,
#     }
#     return render(request, 'adminapp/category_delete.html', content)


class ProductCreateView(SuperUserOnlyMixin, PageTitleMixin, CreateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    form_class = ProductEditForm
    success_url = reverse_lazy('admin:products')
    title = 'продукт/создание'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'продукт/создание'
    #     return context


# @user_passes_test(lambda user: user.is_superuser)
# def product_create(request, pk):
#     title = 'продукт/создание'
#     category = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         product_form = ProductEditForm(request.POST, request.FILES)
#         if product_form.is_valid():
#             product_form.save()
#             return HttpResponseRedirect(reverse('admin:products', args=[pk]))
#     else:
#         product_form = ProductEditForm(initial={'category': category})
#
#     content = {
#         'title': title,
#         'update_form': product_form,
#         'category': category,
#     }
#     return render(request, 'adminapp/product_update.html', content)


class ProductsListView(SuperUserOnlyMixin, PageTitleMixin, ListView):
    model = Product
    template_name = 'adminapp/products.html'
    title = 'админка/продукты'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(object_list=object_list, **kwargs)
    #     context['title'] = 'админка/продукты'
    #     return context


# @user_passes_test(lambda user: user.is_superuser)
# def products(request, pk):
#     title = 'админка/продукт'
#     category = get_object_or_404(ProductCategory, pk=pk)
#     # products_list = Product.objects.filter(category=category_item)
#     products_list = Product.objects.filter(category__pk=pk).order_by('name')
#
#     content = {
#         'title': title,
#         'objects': products_list,
#         'category': category,
#     }
#
#     return render(request, 'adminapp/products.html', content)


# class ProductDetailView(SuperUserOnlyMixin, PageTitleMixin, DetailView):
#     model = Product
#     template_name = 'adminapp/product_read.html'
#     title = 'продукт/подробнее'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'продукт/подробнее'
    #     return context


@user_passes_test(lambda user: user.is_superuser)
def product_read(request, pk):
    title = 'продукт/подробнее'
    product = get_object_or_404(Product, pk=pk)
    content = {
        'title': title,
        'object': product,
    }

    return render(request, 'adminapp/product_read.html', content)

class ProductUpdateView(SuperUserOnlyMixin, PageTitleMixin, UpdateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('admin:product_update')
    form_class = ProductEditForm
    title = 'продукт/редактирование'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'продукт/редактирование'
    #     return context


# @user_passes_test(lambda user: user.is_superuser)
# def product_update(request, pk):
#     title = 'продукт/редактирование'
#
#     edit_product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
#
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin:product_update', args=[edit_product.pk]))
#
#     else:
#         edit_form = ProductEditForm(instance=edit_product)
#
#     content = {
#         'title': title,
#         'update_form': edit_form,
#         'category': edit_product.category,
#     }
#
#     return render(request, 'adminapp/product_update.html', content)


class ProductDeleteViews(SuperUserOnlyMixin, PageTitleMixin, DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'
    success_url = reverse_lazy('admin:products')
    title = 'продукт/удаление'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'продукт/удаление'
    #     return context

# @user_passes_test(lambda user: user.is_superuser)
# def product_delete(request, pk):
#     title = 'продукт/удаление'
#
#     product = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'POST':
#         product.is_active = False
#         product.save()
#         return HttpResponseRedirect(reverse('admin:products', args=product.category.pk))
#
#     content = {
#         'title': title,
#         'product_to_delete': product,
#     }
#
#     return render(request, 'adminapp/product_delete.html', content)
