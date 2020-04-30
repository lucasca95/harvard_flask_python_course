document.addEventListener('DOMContentLoaded', function(){
    // asignar comportamiento al primer boton de la pagina
    document.querySelector('button').onclick = count;
});

let counter = 0;

function count(){
    counter++;
    document.querySelector('#counter').innerHTML = counter;
    if (counter % 10 === 0){
        // Estas comillas especiales permiten formatear un texto. Propio de ES6.
        alert(`Counter is at ${counter}!`);
    }
}