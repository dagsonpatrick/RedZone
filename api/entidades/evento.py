
#JSON Recebido do CORE
# {'type': 3, 'id': '41fcf78f', 'code': 101, 'data': '053B217800000015', 'date': '2020-04-30T21:04:13Z'}

class Evento():

    def __init__(self, type_event, id_event, code, uuid, battery, date):
        self.__type_event = type_event
        self.__id_event = id_event
        self.__code = code
        self.__uuid = uuid
        self.__battery = battery
        self.__date = date


    @property
    def type_event(self):
        return self.__type_event

    @type_event.setter
    def type_event(self, type_event):
        self.__type_event= type_event

    @property
    def id_event(self):
        return self.__id_event

    @id_event.setter
    def id_event(self, id_event):
        self.__id_event= id_event

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code):
        self.__code = code

    @property
    def uuid(self):
        return self.__uuid

    @uuid.setter
    def uuid(self, uuid):
        self.__uuid = uuid

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, battery):
        self.__battery = battery


    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date
