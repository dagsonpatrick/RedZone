class Collaborator():

    def __init__(self,first_name, last_name, email, foto, statusAssociacao):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__foto = foto
        self.__statusAssociacao = statusAssociacao


    @property
    def first_name(self):
        return self.__first_name
    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        self.email = email

    @property
    def foto(self):
        return self.__foto
    @foto.setter
    def foto(self, foto):
        self.__foto = foto

    @property
    def statusAssociacao(self):
        return self.__statusAssociacao
    @statusAssociacao.setter
    def statusAssociacao(self, statusAssociacao):
        self.__statusAssociacao = statusAssociacao