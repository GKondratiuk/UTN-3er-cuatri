package domain;

public enum TipoEscritura {
    CLASICO ("Escritura a mano"),
    MODERNO ("Escritura digital");
    
    private final String descripcion;
    private TipoEscritura (String descripcion){
    this.descripcion = descripcion;
    }
    
    public String getDescripcion(){
        return this.descripcion;
    }

    String getDescripion() {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }
}
