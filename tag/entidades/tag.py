
class Tag():

    def __init__(self, description, uuid, temperature, battery, statusAssociacao):
        self.__description = description
        self.__uuid = uuid
        self.__temperature = temperature
        self.__battery = battery
        self.__statusAssociacao = statusAssociacao

    def __init__(self, description, uuid):
        self.__description = description
        self.__uuid = uuid

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def uuid(self):
        return self.__uuid

    @uuid.setter
    def uuid(self, uuid):
        self.__uuid = uuid

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