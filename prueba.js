        function toString(lista){ // Devuelve una cadena con los elementos de la lista
            let salida = '';
            for(let i = 0; i < lista.length; i++){
                salida += lista[i];
            }
            return salida;
        }
toString('Hola caracola')