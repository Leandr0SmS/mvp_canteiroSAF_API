# MVP Canteiro SAF - API

    API elaborada para conclusão da Sprint Desenvolvimento Full Stack Básico da Pós graduação Engenharia de software da PUC Rio.
Este projeto busca auxiliar no planejamento de sistemas agroflorestais (SAF) que combinem espécies vegetais de diferentes estratos verticais.<br>
A seleção das espécies que irão compor um SAF é de grande importância para sua eficiência.

O projeto permite ao usuário:
- Inserir/Excluir espécies do banco de dados;
- Selecionar uma espécie por estrato para criar um canteiro apresentando informações pertinentes para realizar o planejamento, manejo e colheita do SAF; 

## Descrição

API implementada em Python e Flask com 3 rotas:
- `/planta` => 
    Adiciona uma nova Planta à base de dados. Retorna uma representação da planta.
- `/plantas` => 
    Faz a busca por todas as Plantas cadastradas. Retorna uma representação da listagem de plantas.
- `/canteiro` => 
    Faz a busca das plantas selecionadas de um canteiro a partir da nome de cada planta. Retorna uma representação do canteiro de um SAF.

## Iniciando

### Dependências

Será necessário ter [python]{https://www.python.org/} e todas as libs listadas no `requirements.txt` instaladas.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtual environments](https://docs.python.org/3/library/venv.html).

### Instalando

Instalar dependências descritas no arquivo `requirements.txt`.
```
(env)$ pip install -r requirements.txt
```

### Executando

Executar o comando:
```
(env)$ flask run --host 0.0.0.0 --port 5000
```

> **Banco de Dados** - Será iniciado e carregado com informações pré definidas.

## Autor
 
[Leandro Simões](https://github.com/Leandr0SmS)

## Licença

The MIT License (MIT)
Copyright © 2023 Leandro Simões

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Inspirações

* [PUC-Rio](https://www.puc-rio.br/index.html)
* [CodeCademy](https://www.codecademy.com/)
* [FreeCodeCamp](https://www.freecodecamp.org/learn/)
* [Cepeas](https://www.cepeas.org/)
* [Agenda Gotsch](https://agendagotsch.com/)

