var count = 10;
var loadedCount = 0;
var category = '';

function loadMoreNews() {
    $.ajax({
        url: '',
        data: {
            category: category,
            page: (loadedCount + count) / count
        },
        success: function(response) {
            var news = response;
            if (news.length > 0) {
                for (var i = 0; i < news.length; i++) {
                    var newsItem = '<div class="box col5 ' + news[i].category + '">' +
                        '<h2><a href="/' + news[i].pk + '">' + news[i].title + '</a></h2>' +
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

$('#filtering-nav a').click(function(e) {
    e.preventDefault();
    category = $(this).attr('class');
    loadedCount = 0;
    $('.items').empty();
    loadMoreNews();
});

loadMoreNews();