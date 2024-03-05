package practica1ds;

import java.util.ArrayList;

public abstract class Carrera {
    private String tipo;
    private ArrayList<Bicicleta> bicicletas;

    public Carrera(String tipo) {
        this.tipo = tipo;
        this.bicicletas = new ArrayList<Bicicleta>();
    }
}