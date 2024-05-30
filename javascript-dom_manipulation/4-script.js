let addItem = document.querySelector('#add_item');

addItem.addEventListener('click', function() {
    let ul = document.querySelector('.my_list');
    let li = document.createElement('li');
    li.textContent = 'Item';
    ul.appendChild(li);
});
