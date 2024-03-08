package practica1ds;

import java.util.ArrayList;

public abstract class Carrera extends Thread {
    private String tipo;
    private ArrayList<Bicicleta> bicicletas;

    public Carrera(String tipo) {
        this.tipo = tipo;
        this.bicicletas = new ArrayList<Bicicleta>();
    }

    public Carrera(ArrayList<Bicicleta> bicicletas) {
        this.bicicletas = bicicletas;
    }

    @Override
    public void run() {
        System.out.println("Comienza la carrera de " + tipo);
    }

    private void retirarBicicletaAleatoria() {
        int aleatorio = (int) (Math.random() * bicicletas.size());
        bicicletas.remove(aleatorio);
    }

    public void agregarBicicleta(Bicicleta bicicleta) {
        bicicletas.add(bicicleta);
    }
}