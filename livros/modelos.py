from seguranca.operador import seguranca_operador
class Livros:
    def __init__(self, id_livro, titulo, autor, categoria, quantidade):
        self.titulo = titulo
        self.id = id_livro
        self.autor = autor
        self.categoria = categoria
        self.quantidade = quantidade
class Estante():
    
    def __init__(self):
        self.livros = []
        self.operador = seguranca_operador()

    def adicionar_livro(self, id_livro, titulo, autor, categoria, quantidade):

        livro = Livros(id_livro, titulo, autor, categoria, quantidade)
        
        self.livros.append(livro)

    def efetivar_emprestimo(self,  id_livro):

        for livro in self.livros:
            if livro.id == id_livro:
                if livro.quantidade > 0:
                    livro.quantidade -= 1
                    self.operador.mensagem_info(f"Empréstimo do livro '{livro.titulo}' realizado com sucesso!")
                    return True
                else:
                    self.operador.mensagem_info(f"Não há exemplares disponíveis do livro '{livro.titulo}'.")
                    return False
        self.operador.mensagem_erro(f"Livro com ID {id_livro} não encontrado na estante.")
        return False

    def efetivar_devolucao(self, id_livro):
    
            for livro in self.livros:

                if livro.id == id_livro:
                    if livro.quantidade >= 0:
                        livro.quantidade += 1
                        self.operador.mensagem_info(f"Devolução do livro '{livro.titulo}' realizada com sucesso!")
                        return True
                    
            self.operador.mensagem_erro(f"Livro com ID {id_livro} não encontrado na estante.")
            return False
    



