from dataclasses import dataclass
from datetime import date


@dataclass
class AlunoDTO():

    nome: str
    data_nascimento: date



    """  def __init__(self, nome, data_nascimento):
        self.__nome = nome
        self.__data_nascimento = data_nascimento


   @property
    def nome(self):
        return self.__nome


    @nome.setter
    def nome(self, nome):
        self.__nome = nome



    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
       self.__data_nascimento = data_nascimento

""" 

