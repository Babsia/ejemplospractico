def __gt__(self,otro):
    resultado=self.getmillas()>otro.getmillas()
    return resultado
def __eq__(self,otro):
    resultado=self.getmillas==otro.getmillas()
    return resultado
