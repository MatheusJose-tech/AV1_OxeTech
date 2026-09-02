class Livros:
    def __init__(self, id_livro, titulo, autor, categoria, quantidade):
        self.titulo = titulo
        self.id = id_livro
        self.autor = autor
        self.categoria = categoria
        self.quantidade = quantidade
        self.estado = ""



class Estante():
    
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, id_livro, titulo, autor, categoria, quantidade):

        livro = Livros(id_livro, titulo, autor, categoria, quantidade)
        
        self.livros.append(livro)

    # vou usar a classe biblioteca para fazer o emprestimo, pq ela tem a lista de usuarios e a lista de livros, e a classe estante so tem a lista de livros

    def efetivar_emprestimo(self,  id_livro):
        for livro in self.livros:
            if livro.id == id_livro:
                if livro.quantidade > 0:
                    livro.quantidade -= 1
                    print(f"Empréstimo do livro '{livro.titulo}' realizado com sucesso!")
                    return True
                else:
                    print(f"Não há exemplares disponíveis do livro '{livro.titulo}'.")
                    return False
        print(f"Livro com ID {id_livro} não encontrado na estante.")
        return False

    def imprimir_livros(self):

        livros_organizados = sorted(self.livros, key=lambda organiza: organiza.id)

        for livro in livros_organizados:
            print(f"ID: {livro.id}, Título: {livro.titulo}, Autor: {livro.autor}, Categoria: {livro.categoria}, Quantidade: {livro.quantidade}")



if __name__ == "__main__":
    estante = Estante()
    estante.adicionar_livro(1, "O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia", 5)
    estante.adicionar_livro(2, "1984", "George Orwell", "Distopia", 3)
    estante.adicionar_livro(3, "O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Infantil", 7)

    estante.imprimir_livros()