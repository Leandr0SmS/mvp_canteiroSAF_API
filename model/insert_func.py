from model.estratos import Estrato
from model.plantas import Planta

def insert_estratos(estratos, session):
    for estrato in estratos:
        estrato_data = Estrato(
            nome_estrato=estrato,
            porcentagem_sombra=estratos[estrato]
        )
        # adicionando estrato
        session.add(estrato_data)
        