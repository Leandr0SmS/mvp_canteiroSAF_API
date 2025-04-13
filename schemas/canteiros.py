from pydantic import BaseModel, Field
from typing import List, Optional
from model.plantas import Planta
from model.estratos import Estrato

class PlantaCanteiroSchema(BaseModel):
    espacamento: int
    estrato: str
    nome_planta: str
    sombra: int
    tempo_colheita: int

class PlantasCanteiroSchema(BaseModel):
    plantas: List[PlantaCanteiroSchema] = Field(default_factory=lambda: [
        PlantaCanteiroSchema(
          espacamento=200,
          estrato="emergente",
          nome_planta="Embaúba",
          sombra=20,
          tempo_colheita=1095
          ),
        PlantaCanteiroSchema(
          espacamento=100,
          estrato="alto",
          nome_planta="Jucara",
          sombra=40,
          tempo_colheita=2555
          ),
        PlantaCanteiroSchema(
          espacamento=50,
          estrato="medio",
          nome_planta="Pimenta-do-reino",
          sombra=60,
          tempo_colheita=1460
          ),
        PlantaCanteiroSchema(
          espacamento=40,
          estrato="baixo",
          nome_planta="Abacaxi",
          sombra=80,
          tempo_colheita=730
          )
    ])

class CanteiroSchema(BaseModel):
    """ Define como um novo canteiro deve ser representado
    """
    nome_canteiro: str = "Canteiro1"
    x_canteiro: int = 800
    y_canteiro: int = 200
    plantas_canteiro: PlantasCanteiroSchema


class ListagemCanteirosSchema(BaseModel):
    """ Define como uma listagem dos Canteiro será retornada.
    """
    plantas:List[CanteiroSchema]


class CanteiroDeleteSchema(BaseModel):
    """ Define como deve ser a estrutura que deleta o canteiro. Que será
        com base no nome das plantas.
    """
    nome_canteiro: str = "Canteiro1"


class CanteiroCriaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        com base no nome das plantas.
    """
    nome_canteiro: str = "Meu Canteiro"
    x_canteiro: int = 800
    y_canteiro: int = 300
    id_planta_emergente: int = 11
    id_planta_alto: int = 22
    id_planta_medio: int = 18
    id_planta_baixo: int = 3
    
class CanteiroBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca por nome. Que será
        feita apenas com base no nome do Canteiro.
    """
    nome_canteiro: str = "Canteiro1"

class CanteiroUpdateSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        com base no nome das plantas.
    """
    nome_canteiro: str = "Canteiro1"
    x_canteiro: Optional[int] = None
    y_canteiro: Optional[int] = None
    id_planta_emergente: Optional[int] = None
    id_planta_alto: Optional[int] = None
    id_planta_medio: Optional[int] = None
    id_planta_baixo: Optional[int] = None
    
   
class CanteiroSchemaDestribuido(BaseModel):
    """ Define como um novo canteiro deve ser representado
    """
    nome_canteiro: str = "Canteiro1"
    x_canteiro: int = 800
    y_canteiro: int = 200
    plantas_canteiro: PlantasCanteiroSchema
    plantas_destribuidas: dict = {
    "alto": [
      {
        "diametro": 100,
        "estrato": "alto",
        "nome_planta": "Jucara",
        "posicao": [
          114,
          100
        ],
        "tempo_colheita": 2555
      },
      {
        "diametro": 100,
        "estrato": "alto",
        "nome_planta": "Jucara",
        "posicao": [
          228,
          100
        ],
        "tempo_colheita": 2555
      }
    ],
    "baixo": [
      {
        "diametro": 40,
        "estrato": "baixo",
        "nome_planta": "Abacaxi",
        "posicao": [
          47,
          33
        ],
        "tempo_colheita": 730
      },
      {
        "diametro": 40,
        "estrato": "baixo",
        "nome_planta": "Abacaxi",
        "posicao": [
          94,
          33
        ],
        "tempo_colheita": 730
      }
    ],
    "emergente": [],
    "medio": [
      {
        "diametro": 50,
        "estrato": "medio",
        "nome_planta": "Pimenta-do-reino",
        "posicao": [
          58,
          50
        ],
        "tempo_colheita": 1460
      },
      {
        "diametro": 50,
        "estrato": "medio",
        "nome_planta": "Pimenta-do-reino",
        "posicao": [
          116,
          50
        ],
        "tempo_colheita": 1460
      }
    ]
}


 
class PlantaCanteiroSchema(BaseModel):
    """ Define como uma planta representada em um canteiro
    """
    nome_planta: str = "Bananeira Prata",
    tempo_colheita: int = 420,
    estrato: str = "alto",
    sombra: int = 40,
    espacamento: float = 3.0,
    
       
class ListagemCanteiroSchema(BaseModel):
    """ Define como uma listagem de plantas será retornada.
    """
    canteiro:List[PlantaCanteiroSchema]


def monta_canteiro(plantas_canteiro: tuple[(Planta, Estrato)]):
    """ Retorna uma representação de um canteiro com as plantas e seus estratos.
    """
    result = []
    for info in plantas_canteiro:
        planta, estrato = info
        result.append({
            "nome_planta": planta.nome_planta,
            "tempo_colheita": planta.tempo_colheita,
            "estrato": planta.estrato,
            "sombra": estrato.porcentagem_sombra,
            "espacamento": planta.espacamento,
        })

    return {"plantas": result}

def apresenta_canteiro(
        nome_canteiro,
        x_canteiro,
        y_canteiro,
        plantas_canteiro: tuple[(Planta, Estrato)], 
        dados_grafico,
        ):
    """ Retorna uma representação de um canteiro com as plantas e seus estratos.
    """
    result = []
    for info in plantas_canteiro:
        planta, estrato = info
        result.append({
            "nome_planta": planta.nome_planta,
            "tempo_colheita": planta.tempo_colheita,
            "estrato": planta.estrato,
            "sombra": estrato.porcentagem_sombra,
            "espacamento": planta.espacamento,
        })

    return {
        "nome_canteiro": nome_canteiro,
        "x_canteiro": x_canteiro,
        "y_canteiro": y_canteiro,
        "plantas": result,
        "dados_grafico": dados_grafico
        }
