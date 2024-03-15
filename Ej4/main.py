import customtkinter
from ui.Salpicadero import Salpicadero
from ui.Controles import Controles

import threading


def main():
    controles = Controles()

    salpicadero = Salpicadero(controles, nombre="Salpicadero")
    # Asignamos la función de destruir la primera ventana cuando la segunda se elimina,
    # así conseguimos que se cierren ambas al mismo tiempo
    salpicadero.protocol("WM_DELETE_WINDOW", controles.destroy)

    controles.mainloop()


if __name__ == "__main__":
    main()
