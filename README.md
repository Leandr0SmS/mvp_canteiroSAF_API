# MVP Canteiro SAF - API

O projeto **Canteiro SAF** é uma API RESTful desenvolvida para apoiar o planejamento de Sistemas Agroflorestais (SAFs), facilitando a seleção e organização de espécies vegetais conforme seus respectivos estratos. A escolha adequada das espécies é fundamental para maximizar a eficiência ecológica, produtiva e o manejo sustentável do SAF.

## Funcionalidades

A API oferece operações básicas para o gerenciamento de espécies e geração de canteiros agroflorestais. As principais funcionalidades incluem:

- Cadastro e remoção de espécies do banco de dados;
- Criação de um canteiro SAF com espécies organizadas por estrato;
- Retorno de informações úteis para planejamento, manejo e colheita.

## Tecnologias Utilizadas

- **Linguagem:** Python 3.x  
- **Framework:** Flask  
- **Formato de Resposta:** JSON  
- **Padrão de API:** RESTful

## Endpoints

| Método | Rota        | Descrição                                                                 |
|--------|-------------|---------------------------------------------------------------------------|
| POST   | `/planta`   | Adiciona uma nova espécie ao banco de dados.                             |
| DELETE | `/planta`   | Remove uma espécie existente a partir do nome.                           |
| GET    | `/plantas`  | Retorna todas as espécies cadastradas.                                   |
| GET    | `/canteiro` | Gera um canteiro com uma espécie selecionada para cada estrato vegetal. |

Todas as rotas utilizam formato JSON para envio e recebimento de dados. Em caso de erro, são retornadas mensagens padronizadas com os códigos HTTP correspondentes.

---

## Execução da Aplicação

A aplicação pode ser executada em diferentes ambientes. Abaixo estão descritas as opções de execução com instruções específicas.

- [Ambiente local com Python, venv e pip](#execução-local-com-python)
- [Ambiente containerizado com Docker](#execução-com-docker)

---

### Execução Local com Python

**Pré-requisitos:**

- Python 3.8+ instalado ([Download](https://www.python.org/downloads/))
- `pip` instalado e configurado
- `venv` disponível (nativo a partir do Python 3.3)

**Passos:**

1. Criar e ativar um ambiente virtual:

   ```bash
   python -m venv env
   source env/bin/activate  # Linux/macOS
   .\env\Scripts\activate   # Windows

2. Instalar dependências:

   ```bash
   (env)$ pip install -r requirements.txt

3. Executar a aplicação Flask:

   ```bash
   (env)$ flask run --host 0.0.0.0 --port 5000

A API estará disponível em: [http://localhost:5000](http://localhost:5000)

### Execução com Docker

**Pré-requisitos:**

- [Docker Engine](https://docs.docker.com/engine/install/) instalado e em execução
- Permissões administrativas para build e execução de containers

**Passos:**

1. Criar uma rede Docker (opcional, mas recomendável para futuras integrações entre serviços):

   ```Docker CLI
   docker network create my_network


2. Construir a imagem Docker a partir do `Dockerfile` localizado no diretório raiz do projeto:

   ```Docker CLI
   docker build --no-cache -t meu_canteiro_api .


3. Executar o container com a imagem criada:

   ```Docker CLI
   docker run --name meu_canteiro_api --network my_network -p 5000:5000 meu_canteiro_api


A API estará acessível em: [http://localhost:5000/#/](http://localhost:5000/#/)

## Autor

[Leandro Simões](https://github.com/Leandr0SmS)

## Licença

The MIT License (MIT)
Copyright © 2023 Leandro Simões

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Inspirações

- [PUC-Rio](https://www.puc-rio.br/index.html)
- [CodeCademy](https://www.codecademy.com/)
- [FreeCodeCamp](https://www.freecodecamp.org/learn/)
- [Cepeas](https://www.cepeas.org/)
- [Agenda Gotsch](https://agendagotsch.com/)
