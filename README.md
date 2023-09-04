# MVP Canteiro SAF - API

API elaborada para conclusão da Sprint Desenvolvimento Full Stack Básico da Pós graduação Engenharia de software da PUC Rio.

## Descrição

API implementada em Python e Flask com 3 rotas:
- `/planta` => 
    Adiciona uma nova Planta à base de dados. Retorna uma representação da planta.
- `/plantas` => 
    Faz a busca por todas as Plantas cadastradas. Retorna uma representação da listagem de plantas.
- `/canteiro` => 
    Faz a busca das plantas selecionadas de um canteiro a partir da nome de cada planta. Retorna uma representação do canteiro.

## Iniciando

### Dependências

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://docs.python.org/3/library/venv.html).

### Instalando

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.
```
(env)$ pip install -r requirements.txt
```

### Executando a API

Para executar a API basta executar o comando:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

## Autor
 
[Leandro Simões](https://github.com/Leandr0SmS)

## Licença

   Copyright 2023 Leandro Simões

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

## Inspirações

* [PUC-Rio](https://www.puc-rio.br/index.html)
* [CodeCademy](https://www.codecademy.com/)
* [FreeCodeCamp](https://www.freecodecamp.org/learn/)
* [Cepeas](https://www.cepeas.org/)
* [Agenda Gotsch](https://agendagotsch.com/)

