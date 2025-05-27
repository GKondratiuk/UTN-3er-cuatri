miFuncion1();
miFuncion2();
function miFuncion1(){
    console.log('Funcion 1');
}

function miFuncion2(){
    console.log('Funcion 2');
}

//Funcion de tipo CallBack
function imprimir(mensaje){
    console.log(mensaje);
}

function sumar(op1, op2,funcionCallback){
    let res = op1 + op2;
    funcionCallback(`Resultado: ${res}`)
}

//la funcion sumar agrega los parametros de suma + la funcion imprimir
sumar(5,3,imprimir);

//Lamadas asincronas con el uso setTimeout
function miFuncionCallback(){
    console.log('Saludo asincrono despues de 3 segundos');
}

setTimeout(miFuncionCallback, 3000); //tiempo en milesimas de segundo

setTimeout(function(){console.log('Saludo Asincrono 2')}, 4000);

setTimeout( () => console.log('Saludo asincrono 3'), 5000);

//setInterval llama a la funcion varias veces en un determinado intervalo de tiempo 

let reloj = () => {
    let fecha = new Date();
    console.log(`${fecha.getHours()}:${fecha.getMinutes()}:${fecha.getSeconds()}`)
}

setInterval(reloj, 1000); //Cada 1 segundo se ejecuta