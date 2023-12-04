var count = 10;
var loadedCount = 0;
var category = '';  // Переменная для хранения выбранной категории

function loadMoreNews() {
    $.ajax({
        url: '',
        data: {
            count: count,
            category: category,
            page: (loadedCount + count) / count  // Текущая страница для пагинации
        },
        success: function(response) {
            var news = response;
            if (news.length > 0) {
                for (var i = 0; i < news.length; i++) {
                    var newsItem = '<div class="box col5 ' + news[i].category + '">' +
                        '<h2><a href="http://127.0.0.1:8000/' + news[i].pk + '">' + news[i].title + '</a></h2>' +
                        '<p>' + news[i].content + '</p>' +
                        '</div>';
                    $('.items').append(newsItem);
                }
                loadedCount += count;
            }
        },
        error: function() {
            // Обработка ошибки
        }
    });
}

$(window).scroll(function() {
    if ($(window).scrollTop() + $(window).height() >= $(document).height()) {
        loadMoreNews();
    }
});

// Перехватываем клики по ссылкам фильтрации
$('#filtering-nav a').click(function(e) {
    e.preventDefault();
    category = $(this).attr('class');  // Получение выбранной категории
    loadedCount = 0;  // Сброс счетчика загруженных новостей
    $('.items').empty();  // Очистка контейнера с новостями
    loadMoreNews();  // Загрузка новых новостей с учетом фильтрации
});

loadMoreNews();