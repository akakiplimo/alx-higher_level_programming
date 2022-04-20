$(function () {
    $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, status) {
        if (status === "success") {
            let films = data.results;
            for (let i in films) {
                $('#list_movies').append('<li>' + films[i].title + '</li>');
            }
        }
    });
});
