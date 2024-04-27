import http.client
import random
from flask import Flask, jsonify, request, render_template, redirect, url_for
from db import create_tables, create_book, delete_book, listar_livros, atualizar_livro, obter_livro_id
import json
app = Flask(__name__)


@app.route('/')
def index():
    print("A")
    items = listar_livros()
    print(items)

    for item in items:
        print(item[2])

    return render_template('index.html', items=items)


def select_random_nominee():
    years = list(range(2010, 2025))  # Lista de anos de 2010 a 2024
    # Lista de strings com os anos
    nominees = [f"/nominees/romance/{year}" for year in years]

    # Seleciona aleatoriamente um item da lista de strings
    random_nominee = random.choice(nominees)

    return random_nominee


@app.route('/criartabelas', methods=['GET'])
def create_tablesAPI():
    create_tables()
    return jsonify({'mensagem': 'Tabela criada!'}), 200

# Rota para lidar com a inclusão de um novo item


@app.route('/templatecriarlivro')
def add_item():
    return render_template('templatecriarlivro.html')

@app.route('/templateeditarlivro/<int:id>', methods=['GET'])
def edit_item(id):
    book = obter_livro_id(id)
    return render_template('templateeditarlivro.html', item=book)

@app.route('/visualizarlivro/<int:id>', methods=['GET'])
def see_item(id):

    book = obter_livro_id(id)
    return render_template('visualizarlivro.html', item=book)

@app.route('/visualizarlivroAPI/<int:id>', methods=['GET'])
def see_itemAPI(id):

    book = obter_livro_id(id)
    return jsonify({'Livro selecionado': book}), 200

def remover_arrobas(texto):
    texto_sem_arrobas = texto.replace('@', '')
    return texto_sem_arrobas

@app.route('/criarlivro', methods=['POST'])
def criar_livro():
    nome = request.form.get('nome')
    if nome == None:
        data_book = request.json
        create_book(data_book)
        return jsonify({'mensagem': 'Livro criado!'}), 200
    else:
        num_paginas = request.form.get('num_paginas')
        autor = request.form.get('autor')
        bio = request.form.get('bio')

        data_book = {
        'nome': nome,
        'num_paginas': num_paginas,
        'autor': autor,
        'bio': bio}

        create_book(data_book)
        return redirect(url_for('index'))
    
@app.route('/deletarlivro/<int:id>', methods=['GET'])
def deletar_livro(id):
    delete_book(id)
    return redirect(url_for('index'))


@app.route('/deletarlivroAPI/<int:id>', methods=['DELETE'])
def deletar_livroAPI(id):
    delete_book(id)
    return jsonify({'mensagem': 'Livro deletado!'}), 200


@app.route('/listarlivros', methods=['GET'])
def listar_livrosrota():
    listaLivros = listar_livros()
    print(listaLivros)
    return jsonify({'mensagem': listaLivros}), 200


@app.route('/editarlivros', methods=['PUT', 'POST'])
def editar_livros():
    nome = request.form.get('nome')

    if nome == None and request.method == 'PUT':
        data_book = request.json
        atualizar_livro(data_book)
        return jsonify({'mensagem': "Livro editado!"}), 200
    elif request.method == 'POST':
        num_paginas = request.form.get('num_paginas')
        autor = request.form.get('autor')
        bio = request.form.get('bio')
        id = request.form.get('id')
        data_book = {
            'id' : id,
            'nome': nome,
            'num_paginas': num_paginas,
            'autor': autor,
            'bio': bio}
        print("AAAAAAAAAA")
        print(data_book)
        atualizar_livro(data_book)

        return redirect(url_for('index'))
    


@app.route('/listarlivro/<int:id>', methods=['GET'])
def obter_livro(id):
    livro = obter_livro_id(id)
    return jsonify({'mensagem': livro}), 200


# https://rapidapi.com/roftcomp-laGmBwlWLm/api/hapi-books/
conn = http.client.HTTPSConnection("hapi-books.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "09e317f572mshad40887f7b6c52dp1b021djsn906d44738fc6",
    'X-RapidAPI-Host': "hapi-books.p.rapidapi.com"
}


def is_book_empty(book):
    # Verifica se 'book' é uma lista e se está vazia
    if isinstance(book, list) and not book:
        return True
    else:
        return False


@app.route("/preencherlivros", methods=['GET'])
def preencher():
    count = 0
    while count < 10:
        count += 1

        apiRandomRoute = select_random_nominee()
        print(apiRandomRoute)
        conn.request("GET", apiRandomRoute, headers=headers)
        res = conn.getresponse()
        data = res.read()
        book = json.loads(data)
        print(book)
        if (is_book_empty(book)):
            continue

        fake_book = {
            "nome": book[0]['name'],
            "autor": book[0]['author'],
            "num_paginas": 34,
            "bio": f"{book[0]['name']} por {book[0]['author']}"
        }
        create_book(fake_book)

    return jsonify({'mensagem': "Livros preenchidos"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)