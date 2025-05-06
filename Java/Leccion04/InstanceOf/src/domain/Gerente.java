package domain;

//clase hija Empleado
public class Gerente extends Empleado {
    private String departamento; //metodo
    //constructor de la clase hija
    public Gerente(String nombre, double sueldo, String departamento) {
        super(nombre, sueldo);
        this.departamento = departamento;
    }
    
    //redefine, "sobreeescribe" el metodo de la clase padre obtenerdetalles. para que figure el nuevo parametro departamento
    @Override
    public String obtenerDetalles(){
        return super.obtenerDetalles() + " Departamento: "+this.departamento;
    }

    public String getDepartamento() {
        return departamento;
    }

    public void setDepartamento(String departamento) {
        this.departamento = departamento;
    }
    
    
}
