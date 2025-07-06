
let miPromesa = new Promise((resolver, rechazar) => {
    let expresion = true;
    if(expresion){
        resolver('Resolvió correctamente');
    } else{
        rechazar('Se produjo un error')
    }
});
/*
miPromesa.then(
    valor => console.log(valor),
    error => console.log(error)
);
*/

/*
miPromesa
    .then(valor => console.log(valor))
    .catch(error => console.log(error));
    */



let promesa = new Promise ( (Resolver) =>{
    setTimeout(() => Resolver('Saludos desde promesa, callback, funcion flecha y setTimeout'),3000);
});
//El llamado de la promesa 
//promesa.then(valor => console.log(valor));

//async indica que una funcion regresa una promesa

async function miFuncionConPromesa(){
    return 'Saludos con promesas y asinc'
}

//miFuncionConPromesa().then(valor => console.log(valor));

//ASYNC/AWAIT
async function miFuncionConPromesaYawait(){
    let miPromesa = new Promise(resolver =>{
        resolver('Promesa con await');
});
console.log(await miPromesa)
}

miFuncionConPromesaYawait();

//Promesas, await, async y setTimeout

async function funcionConPromesaAwaitTimeout(){
    let miPromesa = new Promise(resolver =>{
        setTimeout(()=> resolver('Promesa con await y TImeout'),3000)

    });
    console.log(await miPromesa);
}

//llamamos a la funcion
funcionConPromesaAwaitTimeout();