$(document).ready(() => {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.get(url, function (data) {
    $.each(data.results, function (index, film) {
      $('ul#list_movies').append('<li>' + film.title + '</li>');
    });
  });
});
