from pydantic import BaseModel
from typing import Optional, List
from model.plantas import Planta
from model.estratos import Estrato

class PlantaSchema(BaseModel):
    """ Define como uma nova planta a ser inserida deve ser representada
    """
    nome_planta: str = "Bananeira Prata"
    tempo_colheita: int = 420
    estrato: str = "alto"
    espacamento: float = 3.0
 
    
class PlantaBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome da planta.
    """
    nome_planta: str = "Bananeira Prata"


class PlantaViewSchema(BaseModel):
    """ Define como uma planta será retornada: planta.
    """
    id_planta: int = 1
    nome_planta: str = "Bananeira Prata"
    estrato: str = "alto"
    tempo_colheita: int = 420
    espacamento: float = 3.0


class PlantaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome_planta: str
    
    
class ListagemPlantasSchema(BaseModel):
    """ Define como uma listagem de plantas será retornada.
    """
    plantas:List[PlantaSchema]


def apresenta_planta(planta: Planta):
    """ Retorna uma representação do planta seguindo o schema definido em
        ProdutoViewSchema.
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
    
    
class CanteiroBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        com base no nome das plantas.
    """
    id_planta_emergente: str = "11"
    id_planta_alto: str = "22"
    id_planta_medio: str = "18"
    id_planta_baixo: str = "03"

 
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


def apresenta_canteiro(plantas_canteiro: tuple[(Planta, Estrato)]):
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


