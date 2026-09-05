from seguranca.operador import seguranca_operador
class Relatorio:
        def __init__(self, biblioteca):
            self.biblioteca = biblioteca
            self.operador = seguranca_operador()
            
        
        def gerar_relatorio(self):

            self.operador.mensagem_info("Relatórios de Livros:")
            for id_livro, livro in self.biblioteca.livros.items():
                self.operador.mensagem_info(f"Livro: {livro.titulo} (ID: {id_livro})")
                self.operador.mensagem_info(f"Autor: {livro.autor}")
                self.operador.mensagem_info(f"Categoria: {livro.categoria}")
                self.operador.mensagem_info(f"Quantidade em Estoque: {livro.quantidade}")
                print("-" * 30)

            print()
        
        def gerar_relatorio_resumido(self):

            total_usuarios = len(self.biblioteca.usuarios)
            total_livros = len(self.biblioteca.livros)
            total_emprestimos = len(self.biblioteca.emprestimos)
            livros_disponiveis = sum(livro.quantidade for livro in self.biblioteca.livros.values())

            self.operador.mensagem_info("Relatório Resumido:")
            self.operador.mensagem_info(f"Total de Usuários: {total_usuarios}")
            self.operador.mensagem_info(f"Total de Livros:{total_livros - livros_disponiveis} |{livros_disponiveis}")
            self.operador.mensagem_info(f"Total de Empréstimos Ativos: {total_emprestimos}")
