from pydantic import BaseModel
from typing import Optional, List
from model.plantas import Planta
from model.estratos import Estrato


class PlantaSchema(BaseModel):
    """ Define como uma nova planta a ser inserida deve ser representada
    """
    nome_planta: str = "Batata-doce"
    tempo_colheita: int = 140
    estrato: str = "baixo"
    espacamento: float = 0.3
 
    
class PlantaBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome da planta.
    """
    nome_planta: str = "Bananeira Prata"


class PlantaViewSchema(BaseModel):
    """ Define como uma planta será retornada: planta.
    """
    id_planta: int = 12
    nome_planta: str = "Batata-doce"
    estrato: str = "baixo"
    tempo_colheita: int = 140
    espacamento: float = 0.3


class PlantaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome_planta: str
    
    
class ListagemPlantasSchema(BaseModel):
    """ Define como uma listagem das plantas será retornada.
    """
    plantas:List[PlantaSchema]


def apresenta_planta(planta: Planta):
    """ Retorna uma representação da planta seguindo o schema definido em
        PlantaViewSchema.
    """
    return {
        "id_planta": planta.id_planta,
        "nome_planta": planta.nome_planta,
        "tempo_colheita": planta.tempo_colheita,
        "estrato": planta.estrato,
        "espacamento": planta.espacamento,
    }
   
    
def apresenta_plantas(plantas: List[Planta]):
    """ Retorna uma representação de uma planta seguindo o schema definido em
        PlantaViewSchema.
    """
    result = []
    for planta in plantas:
        result.append({
            "id_planta": planta.id_planta,
            "nome_planta": planta.nome_planta,
            "tempo_colheita": planta.tempo_colheita,
            "estrato": planta.estrato,
            "espacamento": planta.espacamento,
        })

    return {"plantas": result}
