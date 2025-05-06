package paquete1;
//public significa que puede ser utilizado en cualquier parte de nuestro 
//protected no aplica para las clases
public class Clase1 {
    //atributo de clase
    public String atributoPublic = "Valor atributo public";
    protected String atributoProtected = "Valor atributo protected";
    
    public Clase1(){
        System.out.println("Constructor public");
    }
    
    protected Clase1(String atributoProtected){
        System.out.println("Constructor protected");
    }
    
    //metodo
    public void metodoPublico(){
        System.out.println("Método public");
    }
    
    protected void metodoProtected(){
        System.out.println("Método protected");
    }
    
}
