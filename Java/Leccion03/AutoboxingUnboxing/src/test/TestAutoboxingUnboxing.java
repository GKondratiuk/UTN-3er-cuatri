package test;

public class TestAutoboxingUnboxing {
    public static void main(String[] args) {
        //Clases envolvenes o Wrapper
        /*
            Clases envolventes de tipos primitivos
            int = la clase envolvente es Integer
            long = la clase envolvente es Long
            float = la clase envolvente es Float
            double = la clase envolvente es Double
            boolean = la clase envolvente es Boolean
            byte = la clase envolvente es Byte
            char = la clase envolvente es Char
            short = la clase envolvente es Short
        */
        
        int enteroPrim = 10; //primitivo
        System.out.println("enteroPrim = " + enteroPrim);
        Integer entero = 10; //objeto
        System.out.println("entero = " + entero);
        System.out.println("entero = " + entero.toString());
        System.out.println("entero = " + entero.doubleValue()); //autoBoxing, pasar de un objeto a primitivo
        
        int entero2 = entero; //Unboxing, se extrae la literal del entero y se asigna a una variable primitiva
        System.out.println("entero2 = " + entero2);
    }
}
