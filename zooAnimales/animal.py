class Animal():
    
    _totalAnimales = 0
    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None

    def movimeinto(self):
        return "desplazarse"
    
    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        from gestion.zona import Zona
        return(f"Mamiferos : {len(Mamifero.getListado())}\nAves : {len(Ave.getListado())}\nReptiles : {len(Reptil.getListado())}\nPeces : {len(Pez.getListado())}\nAnfibios : {len(Anfibio.getListado())}")
    
    def toString(self):
        if self._zona != None:
            return (f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona} , en el zoo {self._zona.getZoo()}")
        
        else:
            return (f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}")

    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
    

    @classmethod
    def sumarAnimal(cls):
        cls._totalAnimales = cls._totalAnimales + 1

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getEdad(self):
        return self._edad
    
    def setEdad(self, edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat
    
    def setHabitat(self, habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero
    
    def setGenero(self, genero):
        self._genero = genero

    def getZona(self):
        return self._zona
    
    def setZona(self, zona):
        self._zona = zona
        