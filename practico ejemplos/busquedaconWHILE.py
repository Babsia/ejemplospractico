def buscar(self, codigo):
        i = 0
        while i < len(self.__lista) and self.__lista[i].getCodigoPlan() != codigo:
            i += 1
        if i == len(self.__lista):
            i = -1
        return i