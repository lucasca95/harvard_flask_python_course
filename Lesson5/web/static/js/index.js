document.addEventListener('DOMContentLoaded', () => {

    // Vamos a usar AJAX solo cuando el form se envie
    document.querySelector('#form').onsubmit = () => {

        // inicializamos un objeto request para hacer el pedido a un servidor externo
        const request = new XMLHttpRequest();
        
        // tomamos el valor del campo input de texto
        const currency = document.querySelector('#currency').value;
         
        // vamos a hacer un request por post a la url /convert
        request.open('POST', '/convert');

        // Cuando el request este hecho, cuando este listo...
        request.onload = () => {
            // Aca adentro y atenemos los parametros que el server nos envio en formato JSON

            // Convertir la respuesta a texto y convertirlo a JSON
            const data = JSON.parse(request.responseText);
            if(data.success){
                const contents = `1 USD = ${data.rate} ${currency}.`;
                document.querySelector('#result').innerHTML = contents;
            }
            else {
                document.querySelector('#result').innerHTML = 'Error';
            }
        };

        // Enviamos informacion al servidor
        const data = new FormData();
        // formato ('key', value)
        data.append('currency', currency);

        // enviar el dato
        request.send(data);
        
        return false;
    };

});