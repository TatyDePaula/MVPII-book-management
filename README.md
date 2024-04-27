# Flask API for Book Management -> BOOK SITE

## Inicializando o projeto
Para instalar as dependências necessárias, vá até a raiz do projeto e acione esse comando no terminal.

` pip install -r requirements.txt `

Para rodar a api pelo terminal, sem o docker, basta executar

` python app.py `

Na raiz do projeto.

## Utilizando o banco de dados
Por padrão, está sendo usado o SQLITE3, mas é possível utilizar o MySQL, apenas configurando o seu uso no arquivo db.py
O SQLITE3 usa o banco de dados no arquivo db.db

## Docker
- Para montar o container, certifique-se que há o arquivo DockerFile configurado dentro da raiz do projeto, e execute o comando
` docker build -t mvpdocker . `
no terminal

## Utilização da API Externa
Link da API Externa -> é necessário fazer o cadastro para obter as chaves key e host para fazer os testes
- https://rapidapi.com/roftcomp-laGmBwlWLm/api/hapi-books/

Em seguida, com as chaves em mão, substitua as chaves que estão no código, em app.py, pelas suas.

` headers = { `
   ` 'X-RapidAPI-Key': "057c61da33mshf7b8c5097cb97c3p11ae3cjsn73d3933dc319", `
   ` 'X-RapidAPI-Host': "hapi-books.p.rapidapi.com" `
` } `

## Rotas

### GET /
- - Descrição: Obter uma lista de todos os livros.
- - Parâmetros: Nenhum.
- - Resposta: Array JSON de objetos de livro.

### GET /listarlivro/{id}
- - Descrição: Obter detalhes de um livro específico por ID.
- - Parâmetros: ID do livro.
- - Resposta: Objeto JSON contendo detalhes do livro.

### POST /criarlivro
- - Descrição: Criar um novo livro.
- - Parâmetros: Objeto JSON com detalhes do livro (nome, num_paginas, autor, bio).
- - Resposta: Objeto JSON confirmando a criação do livro.

### PUT /editarlivros
- - Descrição: Atualizar um livro existente.
- - Parâmetros: Objeto JSON com detalhes atualizados do livro (nome, num_paginas, autor, bio).
- - Resposta: Objeto JSON confirmando a atualização do livro.

### DELETE /deletarlivro/{id}
- - Descrição: Excluir um livro por ID.
- - Parâmetros: ID do livro a ser excluído.
- - Resposta: Objeto JSON confirmando a exclusão do livro.

### GET /preencherlivros
- - Descrição: Preencher o banco de dados com livros fictícios.
- - Parâmetros: Nenhum.
- - Resposta: Objeto JSON confirmando o preenchimento dos livros fictícios.
