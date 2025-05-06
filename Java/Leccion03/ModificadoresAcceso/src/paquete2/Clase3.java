package paquete2;

import paquete1.Clase1;
//protected no aplica para las clases 
public class Clase3 extends Clase1 {
    public Clase3(){
        super("protected");
        this.atributoProtected = "Accedemos desde la clase hija a elementos protected del padre";
        System.out.println("AtributoProtected = " + this.atributoProtected);
        this.atributoPublic = "Es totalmente publico";
    }
}
