package test;

import domain.Empleado;
import domain.Escritor;
import domain.TipoEscritura;
import static domain.TipoEscritura.CLASICO;

public class TestConversionObjetos {
    public static void main(String[] args) {
        Empleado empleado;
        empleado = new Escritor("Juan", 5000, TipoEscritura, CLASICO);
        //System.out.println("empleado = " + empleado);
        System.out.println(empleado.obtenerDetalles());
        //empelado.getTipoEscritura(); - NO SE PUEDE HACER
        //Downcasting
        //((Escritor)empleado).getTipoEscritura();//tenemos 2 opciones. - 1ra - CASTING
        Escritor escritor = (Escritor)empleado; //segunda - CASTING
        escritor.getTipoEscritura();
        
        //Upcasting
        Empleado empleado2 = escritor;
        System.out.println(empleado2.obtenerDetalles());
                
    }
}
