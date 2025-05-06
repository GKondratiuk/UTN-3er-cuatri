class Empleado{
    constructor(nombre,sueldo){
        this._nombre = nombre;
        this._sueldo = sueldo;
    }

    obtenerDetalles(){
        return `Empleado: nombre: ${this._nombre},
        Sueldo: ${this._sueldo}`
    }  
}

class Gerente extends Empleado{
    constructor(nombre, sueldo, departamento){
        super(nombre,sueldo);
        this._departamento = departamento;
    }
    //Agregamos la sobreescritura
    obtenerDetalles(){
        return `Gerente: ${super.obtenerDetalles()} depto: ${this._departamento} `
    }
}
//polimorfismo metodo que se comporta de forma diferente dependiendo del objeto que invoque
function imprimir(tipo){
    console.log(tipo.obtenerDetalles());
    if(tipo instanceof Gerente){ //instanceof verifica el tipo de objeto que se ejecuta
        console.log("Es un objeto de un tipo Gerente")
    }
    else if(tipo instanceof Empleado){
        console.log("Este es un objeto de tipo empleado")
    }
    else if(tipo instanceof Object){
        console.log("es de tipo Object ")
    }
}

gerente1 = new Gerente("Carlos",5000,"Sistemas");
console.log(gerente1); //objeto de la clase hija

let empleado1 = new Empleado("Juan",3000);
console.log(empleado1); //objeto de la clase padre

imprimir(gerente1);
imprimir(empleado1);