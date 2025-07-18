const characterEl = document.querySelector('#character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then((response) => response.json())
  .then((data) => {
    characterEl.textContent = data.name;
  })
  .catch((error) => {
    console.error('Error:', error);
    characterEl.textContent = 'Failed to load movie list.';
  });
