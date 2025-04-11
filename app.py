from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, jsonify
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Planta, Estrato
from schemas import *
from logger import logger
from flask_cors import CORS

import requests
import os

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# API ENV
API_CANTEIRO_URL = os.getenv("API_CANTEIRO_URL", "http://localhost:5001")

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
planta_tag = Tag(name="Planta", description="Adição, visualização e remoção de plantas à base")
canteiro_tag = Tag(name="Canteiro", description="Seleção de plantas da base para criação de um canteiro")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação. 
    
    """
    return redirect('/openapi')


@app.put('/planta', tags=[planta_tag],
          responses={"200": PlantaViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_planta(form: PlantaSchema):
    """Adiciona uma nova Planta à base de dados

    Retorna uma representação da planta.
    """
    planta = Planta(
        nome_planta=form.nome_planta,
        tempo_colheita=form.tempo_colheita,
        estrato=form.estrato,
        espacamento=form.espacamento,
        )
    logger.debug(f"Adicionando planta de nome: '{planta.nome_planta}'")
    try:
        # criando conexão com a base
        with Session() as session:
            # adicionando planta
            session.add(planta)
            session.commit()
            logger.debug(f"Adicionado planta de nome: '{planta.nome_planta}'")
            return apresenta_planta(planta), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Planta de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar planta '{planta.nome_planta}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar nova planta :/"
        logger.warning(f"Erro ao adicionar planta '{planta.nome_planta}', {error_msg}")
        return {"mesage": error_msg}, 400
    
@app.post('/planta', tags=[planta_tag],
            responses={"200": PlantaUpdateSchema, "404": ErrorSchema})
def update_planta(form: PlantaUpdateSchema):
    """
        Edita informações de uma Planta a partir do nome informado

        Retorna uma representação da planta.
    """
    
    planta_nome = unquote(unquote(form.nome_planta))
    logger.debug(f"Editando dados sobre planta #{planta_nome}")
    
    with Session() as session:
        # Buscando planta
        planta_to_updt = session.query(Planta).filter(Planta.nome_planta == planta_nome).first()
        
        if not planta_to_updt:
            error_msg = "Planta não encontrada na base :/"
            logger.warning(f"Erro ao editar planta #'{planta_nome}', {error_msg}")
            return {"message": error_msg}, 404
        
        # Editando atributos
        if form.tempo_colheita is not None:
            planta_to_updt.tempo_colheita = form.tempo_colheita
        if form.estrato is not None:
            planta_to_updt.estrato = form.estrato
        if form.espacamento is not None:
            planta_to_updt.espacamento = form.espacamento
        
        session.commit()
        
        logger.debug(f"Editada planta #{planta_nome}")
        return {"message": "Planta atualizada", "nome_planta": planta_nome}

@app.get('/plantas', tags=[planta_tag],
         responses={"200": ListagemPlantasSchema, "404": ErrorSchema})
def get_plantas():
    """Faz a busca por todas as Plantas cadastradas

    Retorna uma representação da listagem de plantas.
    """
    logger.debug(f"Coletando plantas ")
    # criando conexão com a base
    with Session() as session:
        # fazendo a busca
        plantas = session.query(Planta).all()
        session.commit()

        if not plantas:
            # se não há plantas cadastradas
            return {"plantas": []}, 200
        else:
            logger.debug(f"%d plantas econtrados" % len(plantas))
            # retorna a representação de planta
            return apresenta_plantas(plantas), 200


@app.delete('/planta', tags=[planta_tag],
            responses={"200": PlantaDelSchema, "404": ErrorSchema})
def del_planta(query: PlantaBuscaSchema):
    """Deleta uma Planta a partir do nome da planta informada

    Retorna uma mensagem de confirmação da remoção.
    """
    planta_nome = unquote(unquote(query.nome_planta))
    logger.debug(f"Deletando dados sobre planta #{planta_nome}")
    # criando conexão com a base
    with Session() as session:
        # fazendo a remoção
        del_planta = session.query(Planta).filter(Planta.nome_planta == planta_nome).delete()
        session.commit()
    if del_planta:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado planta #{planta_nome}")
        return {"mesage": "Planta removida", "nome_planta": planta_nome}
    else:
        # se o planta não foi encontrada
        error_msg = "Planta não encontrada na base :/"
        logger.warning(f"Erro ao deletar planta #'{planta_nome}', {error_msg}")
        return {"message": error_msg}, 404
    
@app.put('/canteiro', tags=[canteiro_tag],
         responses={"200": ListagemCanteiroSchema, "404": ErrorSchema})
def get_planta(body: CanteiroBuscaSchema):
    """Faz a busca das plantas selecionadas de um canteiro a partir da nome de cada planta

    Retorna uma representação do canteiro.
    """
    id_planta_emergente = body.id_planta_emergente
    id_planta_alto = body.id_planta_alto
    id_planta_medio = body.id_planta_medio
    id_planta_baixo = body.id_planta_baixo
    
    listaCanteiro = []
    logger.debug(f"""Coletando dados para montar canteiro 
                 #{id_planta_emergente}
                 #{id_planta_alto}
                 #{id_planta_medio}
                 #{id_planta_baixo}
                 """)
    # criando conexão com a base
    with Session() as session:
        # fazendo a busca
        planta_emergente = session.query(Planta, Estrato)\
            .join(Estrato, Planta.estrato == Estrato.nome_estrato)\
            .filter(Planta.id_planta == id_planta_emergente).first()
        listaCanteiro.append(planta_emergente)
        planta_alto = session.query(Planta, Estrato)\
            .join(Estrato, Planta.estrato == Estrato.nome_estrato)\
            .filter(Planta.id_planta == id_planta_alto).first()
        listaCanteiro.append(planta_alto)
        planta_medio = session.query(Planta, Estrato)\
            .join(Estrato, Planta.estrato == Estrato.nome_estrato)\
            .filter(Planta.id_planta == id_planta_medio).first()
        listaCanteiro.append(planta_medio)
        planta_baixo = session.query(Planta, Estrato)\
            .join(Estrato, Planta.estrato == Estrato.nome_estrato)\
            .filter(Planta.id_planta == id_planta_baixo).first()
        listaCanteiro.append(planta_baixo)
        session.commit()

        if not all(tuple is not None for tuple in listaCanteiro):
            # se a planta não foi encontrada
            error_msg = "erro na seleção de plantas para montar o canteiro"
            logger.warning(f"Erro ao montar canteiro '{listaCanteiro}', {error_msg}")
            return {"mesage": error_msg}, 404
        else:

            try:
                # Eviar PUT request
                canteiro_data_init = {
                    "nome_canteiro": body.nome_canteiro,
                    "x_canteiro": body.x_canteiro,
                    "y_canteiro": body.y_canteiro,
                    "plantas_canteiro": monta_canteiro(listaCanteiro)
                }
                
                headers = {
                    'Content-Type': 'application/json',
                }
                response = requests.put(
                    f"{API_CANTEIRO_URL}/canteiro",
                    json=canteiro_data_init,
                    headers=headers
                )
                data_canteiro = response.json()

                # retorna a representação do canteiro
                logger.debug(f"Canteiro montado: '{body.nome_canteiro}'")
                return apresenta_canteiro(
                    data_canteiro['nome_canteiro'],
                    data_canteiro['x_canteiro'],
                    data_canteiro['y_canteiro'],
                    listaCanteiro, 
                    data_canteiro['plantas_destribuidas'],
                    ), 200

            except requests.exceptions.RequestException as e:
                logger.warning(f"Erro ao plotar o canteiro '{body.nome_canteiro}', {error_msg}")
                return {"mesage": error_msg}, 404
            
@app.delete('/canteiros', tags=[canteiro_tag],
            responses={"200": CanteiroDeleteSchema, "404": ErrorSchema})
def del_canteiro(query: CanteiroDeleteSchema):
    """
    Deleta um Canteiro a partir do nome

    Retorna uma mensagem de confirmação da remoção.
    """
    canteiro_nome = unquote(unquote(query.nome_canteiro))
    try:
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.delete(
            f"{API_CANTEIRO_URL}/canteiro",
            params={"nome_canteiro": canteiro_nome},  # Usa como query param
            headers=headers
        )

        if response.status_code == 200:
            data = response.json()
            logger.debug(f"Deletado Canteiro #{canteiro_nome}")
            return data, 200
        elif response.status_code == 404:
            return {"message": "Canteiro não encontrado"}, 404
        else:
            return {"message": "Erro ao deletar canteiro"}, response.status_code

    except Exception as e:
        logger.error(f"Erro ao deletar canteiro '{canteiro_nome}': {str(e)}")
        return {"message": "Erro interno ao deletar canteiro"}, 500
    
@app.get("/canteiros", tags=[canteiro_tag],
         responses={"200": ListagemCanteirosSchema, "500": ErrorSchema})
def listar_canteiros():
    """
    Encaminha a requisição para a API secundária para listar todos os canteiros.
    
    Retorna uma lista com todos os canteiros cadastrados.
    """
    try:
        response = requests.get(f"{API_CANTEIRO_URL}/canteiros")
        
        if response.status_code == 200:
            return response.json(), 200
        else:
            return {
                "message": "Erro ao buscar canteiros na API de canteiros",
                "detalhe": response.text
            }, response.status_code

    except requests.exceptions.RequestException as e:
        logger.error(f"Erro de comunicação com a API de canteiros: {str(e)}")
        return {"message": "Erro de comunicação com a API de canteiros"}, 500
    
@app.post('/canteiro', tags=[canteiro_tag],
          responses={"200": CanteiroUpdateSchema, "400": ErrorSchema, "404": ErrorSchema, "409": ErrorSchema})
def editar_canteiro(form: CanteiroUpdateSchema):
    """
    Encaminha requisição de edição de um canteiro para a API secundária.
    """
    try:
        print(form)
        headers = {"Content-Type": "application/json"}
        response = requests.post(
            f"{API_CANTEIRO_URL}/canteiro",
            json=form.model_dump(),
            headers=headers
        )

        if response.status_code == 200:
            return response.json(), 200
        elif response.status_code == 404:
            return {"message": "Canteiro não encontrado"}, 404
        elif response.status_code == 409:
            return {"message": "Conflito ao editar o canteiro"}, 409
        else:
            return {"message": "Erro ao editar canteiro"}, response.status_code

    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao comunicar com API de canteiro: {str(e)}")
        return {"message": "Erro interno ao tentar editar canteiro"}, 500