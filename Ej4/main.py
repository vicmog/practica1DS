import customtkinter
from clases.Coche import Coche
from ui.Salpicadero import Salpicadero
from ui.Controles import Controles
from clases.Motor import Motor


def main():
    coche = Coche()
    print(coche.estado_motor)

    coche.controles.mainloop()


if __name__ == "__main__":
    main()
