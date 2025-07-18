const addItemEl = document.querySelector("#add_item");

addItemEl.addEventListener('click', () => {
    const li = document.createElement('li');
    li.textContent = 'Item';
    const ul = document.querySelector('.my_list');
    ul.appendChild(li);
})
    ;