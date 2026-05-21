class Pessoa:
    def __init__(self, name=None, cpf=None, email=None, age=None):
        self.__name = name
        self.__cpf = cpf
        self.__email = email
        self.__age = age

    def getName(self):
        return self.__name

    def getCpf(self):
        return self.__cpf

    def getEmail(self):
        return self.__email

    def getAge(self):
        return self.__age
    
    def setName(self, value):
        self.__name = value

    def setCpf(self, value):
        self.__cpf = value

    def setEmail(self, value):
        self.__email = value

    def setAge(self, value):
        self.__age = value