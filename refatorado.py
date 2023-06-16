class Livro:
    # Classe que representa um Livro, contendo título, autor, ano de publicação e disponibilidade.
    def __init__(self, titulo, autor, ano_publicacao):
        # Inicializa um objeto Livro com título, autor, ano de publicação e o estado inicial de disponibilidade como True.
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True

    @property
    def titulo(self):
        # Retorna o título do Livro.
        return self._titulo

    @property
    def autor(self):
        # Retorna o autor do Livro.
        return self._autor

    @property
    def ano_publicacao(self):
        # Retorna o ano de publicação do Livro.
        return self._ano_publicacao

    @property
    def disponivel(self):
        # Retorna a disponibilidade do Livro.
        return self._disponivel

    @disponivel.setter
    def disponivel(self, status):
        # Define a disponibilidade do Livro.
        self._disponivel = status


class Usuario:
    # Classe que representa um Usuário, contendo nome, email e lista de livros emprestados.
    def __init__(self, nome, email):
        # Inicializa um objeto Usuário com nome, email e uma lista vazia de livros emprestados.
        self._nome = nome
        self._email = email
        self._livros_emprestados = []

    @property
    def nome(self):
        # Retorna o nome do Usuário.
        return self._nome

    @property
    def email(self):
        # Retorna o email do Usuário.
        return self._email

    @property
    def livros_emprestados(self):
        # Retorna a lista de livros emprestados pelo Usuário.
        return self._livros_emprestados


class Biblioteca:
    # Classe que representa uma Biblioteca, contendo uma lista de livros e uma lista de usuários.
    def __init__(self):
        # Inicializa um objeto Biblioteca com uma lista vazia de livros e uma lista vazia de usuários.
        self._livros = []
        self._usuarios = []

    @property
    def livros(self):
        # Retorna a lista de livros da Biblioteca.
        return self._livros

    @property
    def usuarios(self):
        # Retorna a lista de usuários da Biblioteca.
        return self._usuarios

    def adicionar_livro(self, livro):
        # Adiciona um livro à lista de livros da Biblioteca.
        self._livros.append(livro)

    def remover_livro(self, livro):
        # Remove um livro da lista de livros da Biblioteca, levanta um ValueError se o livro não estiver na lista.
        if livro not in self._livros:
            raise ValueError(f"Livro '{livro.titulo}' não está na biblioteca.")
        self._livros.remove(livro)

    def buscar_livro(self, titulo):
        # Busca um livro pelo título na lista de livros da Biblioteca, levanta um ValueError se o livro não for encontrado.
        for livro in self._livros:
            if livro.titulo == titulo:
                return livro
        raise ValueError(f"Livro '{titulo}' não encontrado na biblioteca.")

    def adicionar_usuario(self, usuario):
        # Adiciona um usuário à lista de usuários da Biblioteca, levanta um ValueError se o nome do usuário for inválido.
        if usuario.nome == "":
            raise ValueError("Nome de usuário inválido.")
        self._usuarios.append(usuario)

    def remover_usuario(self, usuario):
        # Remove um usuário da lista de usuários da Biblioteca, levanta um ValueError se o usuário não estiver na lista.
        if usuario not in self._usuarios:
            raise ValueError(f"Usuário '{usuario.nome}' não está registrado na biblioteca.")
        self._usuarios.remove(usuario)

    def buscar_usuario(self, nome):
        # Busca um usuário pelo nome na lista de usuários da Biblioteca, levanta um ValueError se o usuário não for encontrado.
        for usuario in self._usuarios:
            if usuario.nome == nome:
                return usuario
        raise ValueError(f"Usuário '{nome}' não encontrado na biblioteca.")

    def realizar_emprestimo(self, usuario, livro):
        # Realiza o empréstimo de um livro para um usuário, levanta um ValueError se o livro não estiver disponível.
        if not livro.disponivel:
            raise ValueError(f"Livro '{livro.titulo}' não está disponível.")
        usuario.livros_emprestados.append(livro)
        livro.disponivel = False

    def realizar_devolucao(self, usuario, livro):
        # Realiza a devolução de um livro por um usuário, levanta um ValueError se o livro não foi emprestado pelo usuário.
        if livro not in usuario.livros_emprestados:
            raise ValueError(f"Livro '{livro.titulo}' não foi emprestado por {usuario.nome}.")
        usuario.livros_emprestados.remove(livro)
        livro.disponivel = True

# Criação de alguns livros
livro1 = Livro("Python para Iniciantes", "John Smith", 2018)
livro2 = Livro("Python Avançado", "Jane Doe", 2020)

# Criação de usuários
usuario1 = Usuario("Alice", "alice@example.com")
usuario2 = Usuario("Bob", "bob@example.com")

# Criação da biblioteca
biblioteca = Biblioteca()

# Adicionar livros à biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

# Adicionar usuários à biblioteca
biblioteca.adicionar_usuario(usuario1)
biblioteca.adicionar_usuario(usuario2)

# Empréstimo de livro
biblioteca.realizar_emprestimo(usuario1, livro1)

# Tentativa de empréstimo de livro indisponível
try:
    biblioteca.realizar_emprestimo(usuario2, livro1)
except ValueError as e:
    print(e)

# Devolução de livro
biblioteca.realizar_devolucao(usuario1, livro1)

# Remoção de livro
biblioteca.remover_livro(livro2)

# Remoção de usuário
biblioteca.remover_usuario(usuario2)

# Busca de livro e usuário
try:
    livro_encontrado = biblioteca.buscar_livro("Python para Iniciantes")
    usuario_encontrado = biblioteca.buscar_usuario("Alice")
    print(livro_encontrado.titulo)
    print(usuario_encontrado.nome)
except ValueError as e:
    print(e)

