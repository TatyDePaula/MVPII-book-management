import mysql.connector
import sqlite3
#db_config = {
#    'host': 'localhost',
 #   'user': 'root',
 #   'password': 'admin',
 #   'database': 'livros',
#}

db_config = {
    'host': 'meu_mysql3',  # Ou 'meu_mysql3' se estiver em um contêiner na mesma rede Docker
    'user': 'user',
    'password': '123',
    'database': 'DBMVP',
}

def create_connection2():
    return mysql.connector.connect(**db_config)

def create_connection():
    return sqlite3.connect('db.db')

def create_tables():

    # CRIA UMA INSTÂNCIA DE CONEXÃO DO BD
    connection = create_connection()

    # Cursor é aquele que executa, fecha, realiza as ações da conexão do BD
    cursor = connection.cursor()

    create_user_table_query = """
    CREATE TABLE IF NOT EXISTS Livros (
        id INTEGER PRIMARY KEY,
        nome VARCHAR(50) NOT NULL,
        autor TEXT,
        num_paginas INT,
        bio VARCHAR(250)
    );
    """

    cursor.execute(create_user_table_query)
    connection.commit()

    cursor.close()
    connection.close()


def create_book(book):
    try:
        print(book)
        connection = create_connection()

        cursor = connection.cursor()

        sql_create_book = f"""
        INSERT INTO livros(
            nome,
            autor,
            num_paginas,
            bio

        )
        Values('{book['nome']}' ,'{book['autor']}','{book['num_paginas']}','{book['bio']}');
        """
        print(sql_create_book)
        cursor.execute(sql_create_book)
        connection.commit()

        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Ocorreu uma exceção: {e}")


def delete_book(id):

    connection = create_connection()

    cursor = connection.cursor()

    sql_delete_book = f"""
        DELETE FROM livros WHERE id = {id};
        """
    cursor.execute(sql_delete_book)
    connection.commit()

    cursor.close()
    connection.close()


def listar_livros():

    connection = create_connection()

    cursor = connection.cursor()

    sql_listar_book = """
        SELECT * FROM livros;
        """
    cursor.execute(sql_listar_book)
    listaLivros = cursor.fetchall()

    connection.commit()
    print(listaLivros)
    cursor.close()
    connection.close()
    return listaLivros


def atualizar_livro(newbook):

    connection = create_connection()

    cursor = connection.cursor()

    sql_update_book = f"""
        UPDATE livros
        SET
        nome = '{newbook['nome']}',
        autor = '{newbook['autor']}',
        num_paginas = '{newbook['num_paginas']}',
        bio = '{newbook['bio']}'
        WHERE id = {newbook['id']};
        """

    cursor.execute(sql_update_book)
    connection.commit()

    cursor.close()
    connection.close()


def obter_livro_id(id):

    connection = create_connection()

    cursor = connection.cursor()

    sql_select_book = f"""
        SELECT * FROM livros WHERE id = {id};
        """
    cursor.execute(sql_select_book)

    livro = cursor.fetchall()

    connection.commit()

    cursor.close()
    connection.close()

    return livro
