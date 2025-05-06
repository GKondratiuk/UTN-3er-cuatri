'use strict'; // mejora la seguridad y ayuda a evitar errores

// x = 10;  variable no definida, no se puede hacer en modo stricto

try{
    x = 10 //esto tampoco se podría hacer, pero lo vamos a atrapar con un try catch
    miFuncion(); //funcion sin definir, tenemos 2 errores en total
    throw 'Mi Error';
}
catch(error){
    console.log(error); // cachamos, capturamos el error y el programa contiunará
}

finally{
    console.log('Termina la revision de errores');
}
console.log('continuamos...');


let resultado = guille;

try{
    y = 5
    if(isNaN(resultado)) throw'No es un numero';
}
catch(error){
    console.log(error);
    console.log(error.name);
    console.log(error.message);
}