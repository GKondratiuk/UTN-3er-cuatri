//FUNCION CLASICA TRADICIONAL
miFuncion();

function miFuncion(){
    console.log("Saludos desde mi funcion");
}

//fUNCION ANONIMA

let myFuncion = function(){
    console.log("Saludos desde la funcion anonima");
}
myFuncion();

//FUNCION FLECHA

let miFuncionFlecha = () =>{
    console.log("Saludos desde mi funcion flecha");
}
miFuncionFlecha();

//lo hacemos en una sola linea
const saludar = () => console.log("Saludos desde funcion flecha resumida");
saludar();

//otro ejemplo
const saludar2 = () =>{
    return "Saludos de funcion 'otro ejemplo'"
}
console.log(saludar2);

//simplificamos 
const saludar3 = () => "Saludamos desde funcion flecha3";
console.log(saludar3);

//probamos con objeto
const regresaObjeto = () => ({nombre:'Juan', apellido: 'Lara'})
console.log(regresaObjeto());

//funcion que recibe parametros
const funcionParametros = (mensaje) => console.log(mensaje);
funcionParametros('Saludos desde funcionParametros');

//funcion clasica
const funcionParametrosClasica = function(mensaje){
    console.log(mensaje);
}
funcionParametrosClasica('Saludos desde la funcion clasica');

//Se pueden omitir los parentesis desde una funcion flecha 
const funcionConParametros = mensaje => console.log(mensaje);
funcionConParametros('Saludos desde otra forma de trabajar con funcion flecha.');

//funcion flecha con varios parametros
const funcionConParametros2 = (op1,op2) => op1 + op2;
console.log(funcionConParametros2(3,5));

//otro modo de escribir
//funcion flecha con varios parametros
const funcionConParametros3 = (op1,op2) => {
    let resultado = op1 + op2;
    return resultado;
}
console.log(funcionConParametros3(1,5));