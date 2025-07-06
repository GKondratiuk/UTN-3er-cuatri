import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ListadoPersonasApp {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        List<Persona> Personas = new ArrayList<Persona>();

        //Menu
        var salir = false;
        while (!salir) {

            mostrarMenu();
            try {
                salir = ejecutarOperacion(entrada, personas);
            } catch (Exception e) {
                System.out.println("Ocurrió un error: " + e.getMessage());
            }
            System.out.println();
        }
    }

    private static void mostrarMenu() {
        //mostramos las opciones
        System.out.print("""
                ****** Listado Personas ******
                1.Agregar. 
                2.Listar.
                3.Salir.
                """);
        System.out.print("Digite una de las opciones: ");
    } //fin del metodo mostrar menu

    private static boolean ejecutarOperacion(Scanner entrada, List<Persona> personas) {
        var opcion = Integer.parseInt(entrada.nextLine());
        var salir = false;
        //revisamos la opcion deigitada a traves de un switch
        switch (opcion) {
            case 1: {//Agrega a las personas
                System.out.print("Digite su nombre: ");
                var nombre = entrada.nextLine();
                System.out.print("Digite su telefono: ");
                var telefono = entrada.nextLine();
                System.out.print("Digite su correo: ");
                var email = entrada.nextLine();
                //creamos el objeto personas
                var persona = new Persona(nombre, tel, email);
                personas.add(persona);
                System.out.println("La lista tiene: " + personas.size() + " elementos");
            }//fin caso 1
            case 2: {//lista a las persoans

            }
        }//fin del switch
    }//fin del metodo ejecutar Operacion
}//fin de la clase