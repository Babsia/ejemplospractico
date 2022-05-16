import numpy
class ManejadorCamas:
    __cantidad = 0
    __dimension = 30
    __incremento = 5
    __camas = None

    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 30
        self.__incremento = 5
        self.__camas = np.empty(30, dtype=Cama)

    
    def agregarCama(self, unaCama):
        if isinstance(unaCama, Cama):
            if self.__cantidad == self.__dimension:
                self.__dimension += self.__incremento
                self.__camas.resize(self.__dimension)
            self.__camas[self.__cantidad] = unaCama
            self.__cantidad += 1

    
    def cargarCSV(self, nombreArchivo):
        archivo = open(nombreArchivo)
        reader = csv.reader(archivo, delimiter=";")
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                unaCama = Cama(fila[0],fila[1], fila[2], fila[3], fila[4], fila[5])
                self.agregarCama(unaCama)