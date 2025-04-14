from pydantic import BaseModel, field_validator
from typing import Optional, List
from model.plantas import Planta

estratos_validos = ["baixo", "medio", "alto", "emergente"]


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
    
class PlantaUpdateSchema(BaseModel):
    """ Define como uma nova planta a ser editada deve ser representada
    """
    nome_planta: str = "Bananeira Prata"
    tempo_colheita: Optional[int] = None 
    estrato: Optional[str] = None 
    espacamento: Optional[float] = None 
    
    @field_validator("tempo_colheita", "espacamento", mode="before")
    @classmethod
    def validate_number(cls, value):
        if isinstance(value, (int, float)): 
            return value
        try:
            return int(value) if "." not in str(value) else float(value)  # Convert valid strings to numbers
        except (ValueError, TypeError):
            return None 
    
    @field_validator("estrato", mode="before")
    @classmethod
    def validate_estrato(cls, value):
        """ Estrato deve ser estratos valido, se não retorna None """
        if isinstance(value, str) and value.lower() in estratos_validos:
            return value.lower()
        return None
    
    
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
