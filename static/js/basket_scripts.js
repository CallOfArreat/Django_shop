window.onload = function () {
    /*
    // можем получить DOM-объект меню через JS
    var menu = document.getElementsByClassName('menu')[0];
    menu.addEventListener('click', function () {
        console.log(event);
        event.preventDefault();
    });
    
    // можем получить DOM-объект меню через jQuery
    $('.menu').on('click', 'a', function () {
        console.log('event', event);
        console.log('this', this);
        console.log('event.target', event.target);
        event.preventDefault();
    });
   
    // получаем атрибут href
    $('.menu').on('click', 'a', function () {
        var target_href = event.target.href;
        if (target_href) {
            console.log('нужно перейти: ', target_href);
        }
        event.preventDefault();
    });
    */

    // добавляем ajax-обработчик для обновления количества товара
    $('.basket_list').on('click', 'input[type="number"]', function () {
        let target_href = event.target;

        if (target_href) {
            $.ajax({
                url: "/basket/edit/" + target_href.name + "/" + target_href.value + "/",

                success: function (data) {
                    $('.basket_list').html(data.result);
                    console.log('ajax done');
                    // return false; это чтобы обновилась корзина и не шел дальше скрипт, чтоб никуда не перекидывало с кнопки, если буду делать AJAX далее корзину и кнопку заказать
                },
            });

        }
        event.preventDefault();
    });

};
// можно и такой вариант запилить плюсом к тому, что выше, чтобы срабатывал перерасчет корзины не только изз-а нажатия
// стрелочки, а и просто при вводе числа количества в корзине. А Ajax вынести в отдельную ф-ию.
// $('.basket_list').on('keyup', 'input[type="number"]', function () {
//     let target_href = event.target;