// Получаем ссылки на элементы фильтра
const filterLinks = document.querySelectorAll('#filtering-nav a');

// При клике на ссылку фильтра
filterLinks.forEach(link => {
  link.addEventListener('click', function(event) {
    // Отменяем обычное поведение ссылки
    event.preventDefault();

    // Получаем значение фильтра из класса ссылки
    const filterValue = this.classList[0];

    // Обновляем URL с параметром запроса
    const currentUrl = new URL(window.location.href);
    currentUrl.searchParams.set('filter', filterValue);

    // Переходим на новый URL
    window.location.href = currentUrl.toString();
  });
});

// При загрузке страницы
window.addEventListener('DOMContentLoaded', function() {
  // Получаем текущее значение параметра запроса "filter" из URL
  const urlParams = new URLSearchParams(window.location.search);
  const currentFilter = urlParams.get('filter');

  // Если есть текущее значение фильтра
  if (currentFilter) {
    // Находим ссылку с соответствующим классом и добавляем активный стиль
    const currentFilterLink = document.querySelector(`#filtering-nav a.${currentFilter}`);
    if (currentFilterLink) {
      currentFilterLink.classList.add('active');
    }
  }
});