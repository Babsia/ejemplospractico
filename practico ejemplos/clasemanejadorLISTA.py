import csv
class manejador:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def cargarlista(self):
        archivo=open('medicamentos.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            objeto=objetos(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],float(fila[6]))
            self.__lista.append(objeto)
        return