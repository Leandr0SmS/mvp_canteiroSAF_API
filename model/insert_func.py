from model.estratos import Estrato
from model.plantas import Planta

def insert_estratos(estratos, session):
    for estrato in estratos:
        estrato_instance = Estrato(
            nome_estrato = estrato,
            porcentagem_sombra = estratos[estrato]
        )
        # adicionando estrato
        session.add(estrato_instance)
        
def insert_plantas(plantas, session):
        for planta in plantas:
            espacamento, estrato, nome_planta, tempo_colheita = [v for v in planta.values()]
            planta_instance = Planta(
                nome_planta = nome_planta,
                tempo_colheita = tempo_colheita,
                estrato = estrato,
                espacamento = espacamento
            )
            # adicionando estrato
            session.add(planta_instance)