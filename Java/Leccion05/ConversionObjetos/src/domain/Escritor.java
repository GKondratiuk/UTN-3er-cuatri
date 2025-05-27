package domain;

public class Escritor extends Empleado {
    final TipoEscritura tipoEscritura;
    
    public Escritor(String nombre, double sueldo, TipoEscritura tipoEscritura){
        super(nombre, sueldo);
        this.tipoEscritura = tipoEscritura;
    }
    //Metodo para sobreescribir
    @Override
    public String obtenerDetalles(){
        return super.obtenerDetalles()+ ", Tipo Escritura: " + tipoEscritura.getDescripion();
    }
    
    @Override
    public String toString(){
    return "Escritor{" + "tipoEscritura=" + tipoEscritura + "}" + " " +super.toString();
    }

    public void getTipoEscritura() {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }
}
