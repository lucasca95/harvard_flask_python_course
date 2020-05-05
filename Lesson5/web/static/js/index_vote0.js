document.addEventListener('DOMContentLoaded', () => {
    // conectar el socker entre el cliente y el server
    // La siguiente linea es standar
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    
    // El objeto socket responde a eventos
    // Cuando el socket se conecte...
    socket.on('connect', () => {
        document.querySelectorAll('button').forEach(button => {
            button.onclick = () => {
                const selection = button.dataset.vote;
                // El objeto socket emite un evento de nombre 'submit vote'
                // Lo que se envía al server es el diccionario que se esta pasando como segundo parámetro
                socket.emit('submit_vote', {'selection': selection})
            };
        });
    });
    socket.on('announce vote', data =>{
        const li = document.createElement('li');
        li.innerHTML = `Vote recorded: ${data.selection}`;
        document.querySelector('#votes').append(li);
    });
});