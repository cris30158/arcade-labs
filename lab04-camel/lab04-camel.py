class Room:
    """
    This is a class that represents the player character.
    """

    def __init__(self,descripcion,norte,sur,este,oeste):
        """ This is a method that sets up the variables in the object. """
        self.descripcion = descripcion
        self.norte = norte
        self.sur = sur
        self.este = este
        self.oeste = oeste

    def printdescripcion(self):
        print(self.descripcion)

dormitorio0=Room("bedroom 0. puedes ir al norte o este",2,None,1,None)
dormitorio1 = Room("bedroom 1. puedes ir al sur,este y salir en el oeste", None, 0, None, -1)
diningroom = Room("dining room. puedes ir al norte, este o oeste", 1, None, 2, 0)


class Game():
    pointer=0
    roomlist = [dormitorio0,dormitorio1,diningroom]
    def __init__(self):
        self.play()

    def ir(self,direccion):
        if direccion is None:
            print("te chocas con la pared por subnormal")
        else:
            self.pointer = direccion

    def play(self):

        while self.pointer != -1:
            currentroom = self.roomlist[self.pointer]
            print("Estás en la habitacion",currentroom.descripcion,". ¿A dónde quieres ir?: ")
            choice=input()

            if choice=="n":
                self.ir(currentroom.norte)

            elif choice =="s":
                self.ir(currentroom.sur)
            elif choice =="e":
                self.ir(currentroom.este)

            elif choice == "o":
                self.ir(currentroom.oeste)

            else:
                print("khe?")
                self.ir(currentroom)

        print("has salido!")





if __name__ == "__main__":
    game=Game()