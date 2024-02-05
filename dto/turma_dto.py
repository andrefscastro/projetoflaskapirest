from dataclasses import dataclass
from datetime import date

@dataclass
class TurmaDTO():

    nome: str
    descricao: str
    data_inicio: date
    data_fim: date
    curso_id: str