from model.estratos import Estrato

def insert_estratos(estratos, session):
    
    for estrato in estratos:
        estrato_data = Estrato(
            nome_estrato=estrato[0],
            porcentagem_sombra=estrato[1]
        )
        # adicionando estrato
        session.add(estrato_data)
