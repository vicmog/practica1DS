/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package practica1ds;

/**
 *
 * @author victo
 */
public class Practica1DS extends Thread {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {

        FactoriaMontana factoriaMontana = new FactoriaMontana();
        FactoriaCarretera factoriaCarretera = new FactoriaCarretera();

        Carrera carreraMontana = factoriaMontana.crearCarrera();
        Carrera carreraCarretera = factoriaCarretera.crearCarrera();

    }

}
