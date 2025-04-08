from sqlalchemy import Column, String, Integer, Float, ForeignKey

from  model import Base


class Planta(Base):
    __tablename__ = 'planta'

    id_planta = Column(Integer, primary_key=True)
    nome_planta = Column(String(140), unique=True, nullable=False)
    tempo_colheita = Column(Integer, nullable=False)
    espacamento = Column(Float, nullable=False)

    # Definição de ForeignKey da tabela estrato.
    estrato = Column(String(50), ForeignKey("estrato.nome_estrato"), nullable=False)

    def __init__(self, nome_planta:str, tempo_colheita:str, estrato:str,
                 espacamento:int):
        """
        Cria uma Planta

        Arguments:
            nome_planta: O nome da planta;
            tempo_colheita: Tempo em dias para colher frutos ou folhas;
            espacamento: Distância entre plantas da mesma espécie;
        """
        self.nome_planta = nome_planta
        self.tempo_colheita = tempo_colheita
        self.estrato = estrato
        self.espacamento = espacamento
        
    def __repr__(self):
        return f'Planta("{self.nome_planta}","{self.estrato}")'
