from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship

from model import Base

class Estrato(Base):
    __tablename__ = 'estrato'

    nome_estrato = Column(String(50), primary_key=True)
    porcentagem_sombra = Column(Integer, nullable=False)

    def __init__(self, nome_estrato:str, porcentagem_sombra:int):
        """
        Cria um Estrato

        Arguments:
            nome_estrato: Nome do estrato;
            porcentagem_sombra: Porcentagem de sombra correspondente à soma das copas das plantas adultas;
        """
        self.nome_estrato = nome_estrato
        self.porcentagem_sombra = porcentagem_sombra
