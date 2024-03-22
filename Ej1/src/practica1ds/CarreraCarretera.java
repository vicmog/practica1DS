package practica1ds;

public class CarreraCarretera extends Carrera {

    public CarreraCarretera(String tipo) {
        super(tipo);
    }

    @Override
    public void run() {
        try {
            System.out.println("Empieza la Carrera de carretera con " + bicicletas.size() + " bicicletas\n");
            Thread.sleep(60000);
            for (int i = 0; i < bicicletas.size() * 0.10; i++) {
                retirarBicicletaAleatoria();
            }

        } catch (InterruptedException e) {

            e.printStackTrace();
        }
    }
}
