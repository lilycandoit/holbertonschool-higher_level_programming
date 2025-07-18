document.addEventListener('DOMContentLoaded', () => {
  const helloEl = document.querySelector('#hello');

  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      helloEl.textContent = data.hello;
    })
    .catch((error) => {
      console.error('Error:', error);
    });
});
