class User():

    def __init__(self, first_name, last_name, email, password, profile_picture):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password
        self.__profile_picture = profile_picture


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
    def password(self):
        return self.__password
    @password.setter
    def password(self, password):
        self.password = password

    @property
    def profile_picture(self):
        return self.__profile_picture

    @profile_picture.setter
    def profile_picture(self, profile_picture):
        self.profile_picture = profile_picture
