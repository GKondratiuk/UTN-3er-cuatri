package test;
//El manejo de excepciones es controlar errores en tiempo de ejecución para evitar que el programa se detenga abruptamente.
//El try catch hay que usarlo solo cuando es extremadamente necesario
import static aritmetic.Aritmetic.division;

public class TestExcepciones {
    public static void main(String[] args) {
        int resultado  = 0;
        try{ //intentamos hacer lo siguiente
            resultado = division(10,2);
        } catch(Exception e){//si no se puede hacer, el programa no se detiene, envía un mensaje  y sigue corriendo
            System.out.println("Ocurrió un error"); 
            e.printStackTrace(System.out); //se imprimirá en consola x q el manual lo pide, es la pila de excepciones
            System.out.println(e.getMessage());
        }
        finally{
            System.out.println("Se revisó la division entre cero"); //se ejecuta siempre
        }
        System.out.println("La variable de resultado tiene como valor: " + resultado);
    }
}
