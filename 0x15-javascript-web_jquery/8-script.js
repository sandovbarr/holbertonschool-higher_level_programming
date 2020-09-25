$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (let iter = 0; iter < data.results.length; iter++) {
    $('#list_movies').append('<li>' + data.results[iter].title + '</li>');
  }
});
