# CRUD FLASK

Estudo sobre manipulação de dados (crud) com ambiente virtual Venv, micro framawork Flask, SQLite, Bootstrap e linguagem de programação Python.

VENV: é um ambiente virtual em Python que isola dependências do projeto, evitando conflitos com pacotes globais do sistema. Ele permite que cada projeto tenha suas próprias bibliotecas e versões específicas.

FRAMEWORK FLASK: é um framework de desenvolvimento web que permite criar aplicações web e APIs usando a linguagem Python. É um microframework, ou seja, um framework leve e flexível que não requer muitas bibliotecas ou ferramentas. 

SQLITE: é um mecanismo de banco de dados SQL autônomo, sem servidor, sem configuração e transacional. Ele armazena os arquivos dentro de sua própria estrutura, o que o torna ideal para aplicações móveis e de baixa complexidade. 

BOOTSTRAP: é um framework front-end gratuito e de código aberto que usa HTML, CSS e JavaScript. 

## FERRAMENTAS UTILIZADAS:
* Linguagem de programação Python.
* Ambiente virtual VENV.
* Framework Flask.
* SQLite.
* Bootstrap.
* Git/GitHub.
* Visual studio code.
* Windows 10.

## MODO DE UTILIZAR:
* Clonar repositório.
* Entrar no diretório do projeto ```cd crud-flask-venv```. 
* Executar ```python -m venv venv``` para instalar o ambiente virtual.
* Executar, caso esteja no Windows, ```venv\Scripts\activate``` para iniciar o ambiente. Caso Linux ou MacOS, ```source venv/bin/activate```.
* Executar ```pip install -r requirements.txt``` para instalar as dependências.
* ```python app.py``` - Executa o algoritmo.
* Para sair do ambiente virtual ```deactivate```.

## CONTRIBUIÇÕES:
Se quiser contribuir para este projeto, fique à vontade para enviar um pull request ou relatar problemas na seção de issues.

## LICENÇA:
Este projeto é licenciado sob a Licença MIT.

## COMANDOS IMPORTANTES
* ```python -m venv venv``` - Cria um ambiente virtual chamado venv. Observação: o primeiro venv é o comando, o segundo, o nome do diretório.
* No Windows, ```venv\Scripts\activate``` e no Linux, ```source venv/bin/activate``` - Inicializa o ambiente.
* ```deactivate``` - Encerra o ambiente.
* ```pip freeze > requirements.txt``` - Gera o arquivo para instalação de dependências. Esse mesmo comando atualiza o arquivo quando uma dependência for instalada.
* ```pip list``` - Lista as dependências do projeto.
* ```pip show``` - Inserindo o nome da dependência após o comando, lista informações da dependência.
* ```pip install -r requirements.txt``` - Instala dependências que estão no arquivo 'requirements.txt'.
* ```pip install``` - Inserindo o nome da dependência após o comando, instala dependências.
* ```pip uninstall``` - Inserindo o nome da dependência após o comando, desinstala dependências.