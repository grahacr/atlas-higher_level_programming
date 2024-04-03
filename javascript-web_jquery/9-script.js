$(document).ready(() => {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.get(url, function (data) {
    const hello = data.hello;
    $('div#hello').text(hello);
  });
});
