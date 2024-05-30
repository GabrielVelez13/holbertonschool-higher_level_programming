document.addEventListener('DOMContentLoaded', (event) => {
    document.querySelector('#btn_translate').addEventListener('click', function() {
        let lang = document.querySelector('#language_code').value;
        fetch(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`)
            .then(response => response.json())
            .then(data => {
                document.querySelector('#hello').textContent = data.hello;
            })
            .catch(error => console.error(error));
    });
});
