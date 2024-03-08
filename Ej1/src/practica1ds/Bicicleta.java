package practica1ds;

public abstract class Bicicleta {

    private String tipo;
    private String identificador;

    public Bicicleta(String tipo, String identificador) {
        this.tipo = tipo;
        this.identificador = identificador;
    }

    public String getTipo() {
        return tipo;
    }

    public String getIdentificador() {
        return identificador;
    }

    public String toString() {
        return "Bicicleta " + tipo + " " + identificador;
    }
}