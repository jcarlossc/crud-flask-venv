from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# Cria instância de Flask. __name__ é o nome do módulo Python atual.
app = Flask(__name__)
# Variável do banco de dados.
BASEDADOS = 'database.db'

# Função responsável pela criação da tabela cliente.
def iniciar_db():
    try:
        '''
             O bloco with (Gerenciador de Contexto) é a garantia 
             de que a porta sempre será fechada após o uso, 
             mantendo o código seguro e organizado.
             O comando CREATE criará uma tabela caso 
             não exista.
        '''
        with sqlite3.connect(BASEDADOS) as conexao:
            conexao.execute('''
                CREATE TABLE IF NOT EXISTS cliente (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    cpf TEXT NOT NULL,
                    email TEXT NOT NULL                                 
                    )
                ''')
    except:
        print("Erro de conexão.")        


# Rota principal - listar clientes.
@app.route('/')
def index():
    try:
        '''
             O bloco with (Gerenciador de Contexto) é a garantia 
             de que a porta sempre será fechada após o uso, 
             mantendo o código seguro e organizado.
             Cria-se uma variável cliente com a consulta SELECT e a 
             envia para index.
        '''
        with sqlite3.connect(BASEDADOS) as conexao:
            cliente = conexao.execute("SELECT * FROM cliente").fetchall()
        return render_template('index.html', cliente = cliente)    
    except:
        print("Erro de conexão.") 


# Rota para criar o cliente.
@app.route('/criar', methods = ['GET', 'POST'])
def criar():
    # Recebe às variáveis via POST.
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']
        try:
            '''
                O bloco with (Gerenciador de Contexto) é a garantia 
                de que a porta sempre será fechada após o uso, 
                mantendo o código seguro e organizado.
                Execulta o comando INSERT para inserir os 
                dados no banco.
            '''
            with sqlite3.connect(BASEDADOS) as conexao:
                conexao.execute("INSERT INTO cliente (nome, cpf, email) VALUES (?, ?, ?)", (nome, cpf, email))
            return redirect(url_for('index'))
        except:
            print("Erro de conexão.") 
    return render_template('criar.html')


# Rota para editar o cliente.
@app.route('/editar/<int:cliente_id>', methods = ['GET', 'POST'])
def editar(cliente_id):
    try:
        '''
             O bloco with (Gerenciador de Contexto) é a garantia 
             de que a porta sempre será fechada após o uso, 
             mantendo o código seguro e organizado.
             Recebe às variáveis via POST, atualiza o banco de dados
             com o comando UPDATE e redireciona para index.
        '''
        with sqlite3.connect(BASEDADOS) as conexao:
            if request.method == 'POST':
                nome = request.form['nome']
                cpf = request.form['cpf']
                email = request.form['email']
                conexao.execute("UPDATE cliente SET nome = ?, cpf = ?, email = ? WHERE id = ?", (nome, cpf, email, cliente_id))
                return redirect(url_for('index'))
            cliente = conexao.execute("SELECT * FROM cliente WHERE id = ?", (cliente_id,)).fetchone()
        return render_template('editar.html', cliente = cliente)    
    except:    
        print("Erro de conexão.") 


# Rota para excluir o cliente.
@app.route('/apagar/<int:cliente_id>')
def apagar(cliente_id):
    try:
        '''
             O bloco with (Gerenciador de Contexto) é a garantia 
             de que a porta sempre será fechada após o uso, 
             mantendo o código seguro e organizado.
             Apaga o cliente com o comando DELETE e 
             redireciona para index.
        '''
        with sqlite3.connect(BASEDADOS) as conexao:
            conexao.execute("DELETE FROM cliente WHERE id = ?", (cliente_id,))
        return redirect(url_for('index'))    
    except:
        print("Erro de conexão.")    

# O Flask irá iniciar um servidor local na porta 5000 
if __name__ == '__main__':
    # Função que criará a tabela cliente.
    iniciar_db()
    app.run(debug = True)