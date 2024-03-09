package practica1ds;

import java.util.ArrayList;

public abstract class Carrera implements Runnable {
    protected String tipo;
    protected ArrayList<Bicicleta> bicicletas;

    public Carrera(String tipo) {
        this.tipo = tipo;
        this.bicicletas = new ArrayList<Bicicleta>();
    }

    public Carrera(ArrayList<Bicicleta> bicicletas) {
        this.bicicletas = bicicletas;
    }

    @Override
    public void run() {
    }

    public void retirarBicicletaAleatoria() {
        int aleatorio = (int) (Math.random() * bicicletas.size());
        bicicletas.remove(aleatorio);
        System.out.println("Se ha retirado la bicicleta nº: " + aleatorio + " de la carrera de " + tipo + "\n");
    }

    public void agregarBicicleta(Bicicleta bicicleta) {
        bicicletas.add(bicicleta);
    }
}