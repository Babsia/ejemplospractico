def __add__(self,millas):
        otroviajero=viajeroFrecuente(self.getnum(),self.getdni(),self.getnom(),self.getape(),self.getmillas()+millas)
        return otroviajero
def __sub__(self,millas):
    otroviajero=viajeroFrecuente(self.getnum(),self.getdni(),self.getnom(),self.getape(),self.getmillas()-millas)
    return (otroviajero)