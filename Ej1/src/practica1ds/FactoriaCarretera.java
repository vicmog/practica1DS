package practica1ds;

public class FactoriaCarretera implements FactoriaCarreraYBicicleta {

    @Override
    public Carrera crearCarrera() {
        CarreraCarretera carrera = new CarreraCarretera("Carretera");
        return carrera;
    }

    @Override
    public Bicicleta crearBicicleta() {
        BicicletaCarretera bicicleta = new BicicletaCarretera("Carretera", "id2");
        return bicicleta;
    }

}
