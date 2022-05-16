def __radd__(self,milla):
    otroviajero=viajeroFrecuente(self.getnum(),self.getdni(),self.getnom(),self.getape(),self.getmillas()+milla)
    return (otroviajero)
def __rsub__(self,millas):
    otroviajero=viajeroFrecuente(self.getnum(),self.getdni(),self.getnom(),self.getape(),self.getmillas()-millas)
    return (otroviajero)