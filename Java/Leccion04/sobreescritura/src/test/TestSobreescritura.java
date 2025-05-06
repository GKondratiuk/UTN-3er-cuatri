package test;

import domain.*;

public class TestSobreescritura {
    
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Juan",10000);
        imprimir(empleado1);
        //System.out.println("empleado1 = " + empleado1.obtenerDetalles());//se muestra como deberia
        //Gerente gerente1 = new Gerente("Jose",5000,"Sistemas"); //sin el override no aparecería el departamento --"SOBREESCRITURA"
        //imprimir(gerente1);
        empleado1 = new Gerente("Jose",5000,"Sistemas"); //nos ahorramos 1 variable escribiendo de esta manera
        imprimir(empleado1);
        
        //System.out.println("gerente1 = " + gerente1.obtenerDetalles());
    }
    //METODO POLIMORFISMO
    public static void imprimir(Empleado empleado){ //Se va a ejecutar desde clase empleado o gerente
        String detalles = empleado.obtenerDetalles();
        System.out.println("detalles = " + detalles);
    }
}
