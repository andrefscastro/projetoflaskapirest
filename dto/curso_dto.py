from dataclasses import dataclass
from datetime import date

@dataclass
class CursoDTO():
    nome:str
    disciplinas: list