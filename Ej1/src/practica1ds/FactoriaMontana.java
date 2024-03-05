package practica1ds;

public class FactoriaMontana implements FactoriaCarreraYBicicleta {

    @Override
    public Carrera crearCarrera() {
        CarreraMontana carrera = new CarreraMontana("Montana");
        return carrera;
    }

    @Override
    public Bicicleta crearBicicleta() {
        BicicletaMontana bicicleta = new BicicletaMontana("Montana", "id1");
        return bicicleta;
    }

}
