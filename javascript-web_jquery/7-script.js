$(document).ready(() => {
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  $.get(url, function (data) {
    const characterName = data.name;
    $('div#character').text(characterName);
  });
});