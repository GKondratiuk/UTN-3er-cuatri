package excepciones;

public class OperacionExcepcion extends RuntimeException { //clase exception, heredamos eso
    //constructor
    public OperacionExcepcion (String mensaje){
    super(mensaje);
    }
}
