package practica1ds;

public class FactoriaMontana implements FactoriaCarreraYBicicleta {

    @Override
    public Carrera crearCarrera() {
        CarreraMontana carrera = new CarreraMontana("Montaña");
        return carrera;
    }

    @Override
    public Bicicleta crearBicicleta(String id) {
        BicicletaMontana bicicleta = new BicicletaMontana("Montaña", id);
        return bicicleta;
    }

}
