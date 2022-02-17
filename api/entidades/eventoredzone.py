
class EventosRedZone():
# {'portal': '01', 'address': 3, 'sentido': 'Saiu', 'timestamp': '2020-04-30T21:04:13.451Z', 'temperature': 25, 'battery': 98}

    def __init__(self, portal , tag, collaborator, sentido, temperature, battery, status, timestamp):
        self.__portal = portal
        self.__tag = tag
        self.__collaborator = collaborator
        self.__sentido = sentido
        self.__temperature = temperature
        self.__battery = battery
        self.__status = status
        self.__timestamp = timestamp

    @property
    def portal(self):
        return self.__portal
    @portal.setter
    def portal(self,portal):
        self.__portal = portal

    @property
    def tag(self):
        return self.__tag
    @tag.setter
    def tag(self, tag):
        self.__tag = tag

    @property
    def collaborator(self):
        return self.__collaborator
    @collaborator.setter
    def collaborator(self, collaborator):
        self.__collaborator = collaborator

    @property
    def sentido(self):
        return self.__sentido
    @sentido.setter
    def sentido(self, sentido):
        self.__sentido = sentido

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
    def status(self):
        return self.__status
    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def timestamp(self):
        return self.__timestamp
    @timestamp.setter
    def timestamp(self, timestamp):
        self.__timestamp = timestamp