const headerEl = document.querySelector("header");

const updateHeaderEl = document.querySelector("#update_header");

updateHeaderEl.addEventListener('click', () => {
    headerEl.textContent = "New Header!!!"
})