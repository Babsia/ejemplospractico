def determinarmillas(self,):
    unviajero=self.__lista[0]
    for viajero in self.__lista:
        if viajero > unviajero:
            unviajero=viajero
    if unviajero==self.__lista[0]:
        resultado=self.__lista[0]
    else:
        resultado=unviajero
    print ("viajero con mas millas es {}".format(resultado.getnum()))
    