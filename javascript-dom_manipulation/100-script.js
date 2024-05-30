document.addEventListener('DOMContentLoaded', function() {
    let my_list = document.querySelector('.my_list');
    let addItem = document.querySelector('#add_item');
    let removeItem = document.querySelector('#remove_item');
    let clearList = document.querySelector('#clear_list');

    addItem.addEventListener('click', function() {
        item = document.createElement('li');
        item.textContent = 'Item';
        my_list.appendChild(item);
    });

    removeItem.addEventListener('click', function() {
        if (my_list.lastElementChild) {
            my_list.removeChild(my_list.lastElementChild);
        }
    });

    clearList.addEventListener('click', function() {
        while (my_list.firstElementChild) {
            my_list.removeChild(my_list.firstElementChild);
        }
    });
});
