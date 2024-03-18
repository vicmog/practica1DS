import threading

from clases.Coche import Coche


def main():
    coche = Coche()
    print(coche.estado_motor)

    threading.Thread(target=coche.update).start()
    coche.controles.mainloop()


if __name__ == "__main__":
    main()
