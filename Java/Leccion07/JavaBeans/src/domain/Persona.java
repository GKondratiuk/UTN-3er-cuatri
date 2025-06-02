package domain;
//JavaBeans =Un JavaBean es una clase Java reutilizable que sigue ciertas convenciones para que otras 
//herramientas (como frameworks, servidores o IDEs) puedan manipularla fácilmente.
import java.io.Serializable;
//La implementación de Serializable en Java permite que un objeto pueda convertirse en una secuencia de bytes, lo que habilita
public class Persona implements Serializable{ //a recuperar y guardar el objeto
    private String nombre; //los atributos tienen que ser privados
    private String apellido;

    //Constructor vacío -OBLIGATORIO
    public Persona(){
    
    }
    
    public Persona(String nombre, String apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
//OBLIGATORIO QUE ESTEN TODOS LOS GETTERS AND SETTERS Y QUE ESTEN ENCAPSULADOS
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }
    
    //complementos - to string
    @Override
    public String toString() {
        return "Persona{" + "nombre=" + nombre + ", apellido=" + apellido + '}';
    }
    
    
}

