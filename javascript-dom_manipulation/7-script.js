fetch('https://swapi-api.hbtn.io/api/films/?format=json').then(response => response.json()).then(data => {
    let listMovies = document.querySelector('#list_movies');
    data.results.forEach(movie => {
        let ul = document.createElement('ul');
        ul.textContent = movie.title;
        listMovies.appendChild(ul);
  });
});
