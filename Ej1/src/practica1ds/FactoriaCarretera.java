package practica1ds;

public class FactoriaCarretera implements FactoriaCarreraYBicicleta {

    @Override
    public Carrera crearCarrera() {
        CarreraCarretera carrera = new CarreraCarretera("Carretera");
        return carrera;
    }

    @Override
    public Bicicleta crearBicicleta(String id) {
        BicicletaCarretera bicicleta = new BicicletaCarretera("Carretera", id);
        return bicicleta;
    }

}
