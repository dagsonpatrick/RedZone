class AssociarAnchor():

    def __init__(self, plano, anchor):
        self.__plano = plano
        self.__anchor = anchor

    @property
    def plano(self):
        return self.__plano
    @plano.setter
    def plano(self,plano):
        self.__plano = plano

    @property
    def anchor(self):
        return self.__anchor
    @anchor.setter
    def anchor(self, anchor):
        self.__anchor = anchor