class AssociarAtivo():

    def __init__(self, tag, ativo):
        self.__tag = tag
        self.__ativo = ativo

    @property
    def tag(self):
        return self.__tag
    @tag.setter
    def tag(self, tag):
        self.__tag = tag

    @property
    def ativo(self):
        return self.__ativo
    @ativo.setter
    def ativo(self, ativo):
        self.__ativo = ativo