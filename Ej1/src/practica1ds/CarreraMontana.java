package practica1ds;

public class CarreraMontana extends Carrera {

    public CarreraMontana(String tipo) {
        super(tipo);
    }

    @Override
    public void run() {
        try {
            System.out.println("Empieza la Carrera de montaña con " + bicicletas.size() + " bicicletas \n");
            Thread.sleep(6000);

            for (int i = 0; i < bicicletas.size() * 0.20; i++) {
                retirarBicicletaAleatoria();
            }

        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

}
