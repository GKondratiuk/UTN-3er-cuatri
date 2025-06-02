package aritmetic;

import excepciones.OperacionExcepcion;

public class Aritmetic {
    public static int division(int numerador, int denominador)
            throws OperacionExcepcion{ // ver package "excepciones"
        if(denominador == 0){
            throw new OperacionExcepcion("Diviosion entre 0"); //lanza un error si entra al fi
    }
        return numerador / denominador;
    }
    
}
