
class Tag():

    def __init__(self, description, address, temperature, battery, statusAssociacao):
        self.__description = description
        self.__address = address
        self.__temperature = temperature
        self.__battery = battery
        self.__statusAssociacao = statusAssociacao

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def temperature(self):
        return self.__temperature
    @temperature.setter
    def temperature(self, temperature):
        self.__temperature = temperature

    @property
    def battery(self):
        return self.__battery
    @battery.setter
    def battery(self, battery):
        self.__battery = battery

    @property
    def statusAssociacao(self):
        return self.__statusAssociacao

    @statusAssociacao.setter
    def statusAssociacao(self, statusAssociacao):
        self.__statusAssociacao = statusAssociacao