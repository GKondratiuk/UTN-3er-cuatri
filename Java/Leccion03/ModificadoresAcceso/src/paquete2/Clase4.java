package paquete2;

public class Clase4 {

    private String atributoPrivate = "atributoPrivado";

    private Clase4() {
        System.out.println("Constructor Privado");

    }

    //creamos un construcor public para poder crear objetos
    public Clase4(String argumento) {//aqui se puede llamar al constructor vacio
        this();
        System.out.println("Constructor publico");
    }

    //metodo private
    private void metodoPrivado() {
        System.out.println("Metodo Privado");

    }

    public String getAtributoPrivate() {
        return atributoPrivate;
    }

    public void setAtributoPrivate(String atributoPrivate) {
        this.atributoPrivate = atributoPrivate;
    }
}
