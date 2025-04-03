from pydantic import BaseModel
from typing import List
from model.plantas import Planta
from model.estratos import Estrato


class CanteiroBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        com base no nome das plantas.
    """
    nome_canteiro: str = "Meu Canteiro"
    x_canteiro: int = 800
    y_canteiro: int = 300
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
        plantas_canteiro: tuple[(Planta, Estrato)], 
        dados_grafico,
        nome_canteiro,
        x_canteiro,
        y_canteiro
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
        "plantas": result,
        "nome_canteiro": nome_canteiro,
        "x_canteiro": x_canteiro,
        "y_canteiro": y_canteiro,
        "dados_grafico": dados_grafico
        }
