from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError
from sqlalchemy import func

from model import Session, Planta, Estrato
from schemas import *
from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
planta_tag = Tag(name="Planta", description="Adição, visualização e remoção de plantas à base")
canteiro_tag = Tag(name="Canteiro", description="Seleção de plantas da base para criação de um canteiro")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/planta', tags=[planta_tag],
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
    try:
        # criando conexão com a base
        with Session() as session:
            # adicionando planta
            session.add(planta)
            session.commit()
            return apresenta_planta(planta), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Planta de mesmo nome já salvo na base :/"
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar nova plnata :/"
        return {"mesage": error_msg}, 400


@app.get('/plantas', tags=[planta_tag],
         responses={"200": ListagemPlantasSchema, "404": ErrorSchema})
def get_plantas():
    """Faz a busca por todas as Plantas cadastradas

    Retorna uma representação da listagem de plantas.
    """
    # criando conexão com a base
    with Session() as session:
        # fazendo a busca
        plantas = session.query(Planta).all()
        session.commit()

        if not plantas:
            # se não há produtos cadastrados
            return {"plantas": []}, 200
        else:
            # retorna a representação de planta
            return apresenta_plantas(plantas), 200


@app.get('/canteiro', tags=[canteiro_tag],
         responses={"200": ListagemCanteiroSchema, "404": ErrorSchema})
def get_planta(query: CanteiroBuscaSchema):
    """Faz a busca das plantas selecionadas de um canteiro a partir da nome de cada planta

    Retorna uma representação do canteiro.
    """
    nome_planta_emergente = query.nome_planta_emergente
    nome_planta_alto = query.nome_planta_alto
    nome_planta_medio = query.nome_planta_medio
    nome_planta_baixo = query.nome_planta_baixo
    
    listaCanteiro = []
    # criando conexão com a base
    with Session() as session:
        # fazendo a busca
        planta_emergente = session.query(Planta, Estrato)\
            .join(Estrato, Planta.estrato == Estrato.nome_estrato)\
            .filter(Planta.nome_planta == nome_planta_emergente).first()
        listaCanteiro.append(planta_emergente)
        planta_alto = session.query(Planta, Estrato)\
            .join(Estrato, Planta.estrato == Estrato.nome_estrato)\
            .filter(Planta.nome_planta == nome_planta_alto).first()
        listaCanteiro.append(planta_alto)
        planta_medio = session.query(Planta, Estrato)\
            .join(Estrato, Planta.estrato == Estrato.nome_estrato)\
            .filter(Planta.nome_planta == nome_planta_medio).first()
        listaCanteiro.append(planta_medio)
        planta_baixo = session.query(Planta, Estrato)\
            .join(Estrato, Planta.estrato == Estrato.nome_estrato)\
            .filter(Planta.nome_planta == nome_planta_baixo).first()
        listaCanteiro.append(planta_baixo)
        session.commit()

        if not all(tuple is not None for tuple in listaCanteiro):
            # se o produto não foi encontrado
            print(listaCanteiro)
            error_msg = "erro na seleção de plantas"
            return {"mesage": error_msg}, 404
        else:
            # retorna a representação de produto
            print(listaCanteiro)
            return apresenta_canteiro(listaCanteiro), 200


@app.delete('/planta', tags=[planta_tag],
            responses={"200": PlantaDelSchema, "404": ErrorSchema})
def del_planta(query: PlantaBuscaSchema):
    """Deleta uma Planta a partir do nome da planta informada

    Retorna uma mensagem de confirmação da remoção.
    """
    planta_nome = unquote(unquote(query.nome_planta))
    print(planta_nome)
    # criando conexão com a base
    with Session() as session:
        # fazendo a remoção
        count = session.query(Planta).filter(Planta.nome_planta == planta_nome).delete()
        session.commit()
    if count:
        # retorna a representação da mensagem de confirmação
        return {"mesage": "Planta removida", "id": planta_nome}
    else:
        # se o planta não foi encontrada
        error_msg = "Planta não encontrado na base :/"
        return {"message": error_msg}, 404