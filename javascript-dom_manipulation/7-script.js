const listEl = document.querySelector('#list_movies');

fetch('https://swapi-api.hbtn.io/api/films/')
  .then((response) => response.json())
  .then((data) => {
    console.log(data);
    const films = data.results;
    films.forEach((film) => {
      const li = document.createElement('li');
      li.textContent = film.title;

      listEl.appendChild(li);
    });
  })
  .catch((error) => {
    console.error('Error:', error);
    listEl.textContent = 'Failed to load movie list.';
  });
