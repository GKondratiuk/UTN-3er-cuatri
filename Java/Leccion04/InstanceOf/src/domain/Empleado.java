package domain;

//Ckase Padre
public class Empleado {
    protected String nombre; 
    protected double sueldo;

//constructor
    public Empleado(String nombre, double sueldo){
        this.nombre = nombre;
        this.sueldo = sueldo;
    }
    
//metodo para la sobreEscritura
    public String obtenerDetalles(){
        return "Nombre: " + this.nombre+", Sueldo: "+this.sueldo;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }
    
}