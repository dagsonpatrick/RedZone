class AssociarCollaborator():

    def __init__(self, tag, collaborator):
        self.__tag = tag
        self.__collaborator = collaborator


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