from gestion import zona
from zooAnimales.animal import Animal
class Reptil(Animal):

    _listado = []
    iguanas = 0
    serpientes = 0
    def __init__(self, nombre, edad, habitat, genero, coloresccamas, largocola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = coloresccamas
        self._largoCola = largocola
        Reptil._listado.append(self)

    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)
    
    def movimeinto(self):
        return "reptar"
    
    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        reptil = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        cls.iguanas = cls.iguanas + 1
        return reptil
    
    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        reptil = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        cls.serpientes = cls.serpientes + 1
        return reptil

    @classmethod
    def getListado(cls):
        return cls._listado
    
    @classmethod
    def setListado(cls, reptil):
        cls._listado.append(reptil)

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, colorescamas):
        self._colorEscamas = colorescamas

    def getLargoCola(self):
        return self._largoCola
    
    def setLargoCola(self, largocola):
        self._largoCola = largocola

    