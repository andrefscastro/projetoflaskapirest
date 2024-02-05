from dataclasses import dataclass
from datetime import date

@dataclass
class ProfessorDTO():

    nome: str
    data_nascimento: date