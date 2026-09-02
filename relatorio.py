class Relatorio:
        def __init__(self, biblioteca):
            self.biblioteca = biblioteca
            
        
        def gerar_relatorio(self):

            print("Relatórios de Livros:")
            for id_livro, livro in self.biblioteca.livros.items():
                print(f"Livro: {livro.titulo} (ID: {id_livro})")
                print(f"Autor: {livro.autor}")
                print(f"Categoria: {livro.categoria}")
                print(f"Quantidade em Estoque: {livro.quantidade}")
                print("-" * 30)
            print()
            print()
            print("Relatório de Empréstimos:")
            for id_usuario, usuario in self.biblioteca.usuarios.items():
                print(f"Usuário: {usuario.nome} (ID: {id_usuario})")
                print(f"Tipo: {usuario.tipo}")
                print(f"Empréstimos Ativos: {usuario.emprestimos_ativos}")
                print(f"Bloqueado: {'Sim' if usuario.bloqueado else 'Não'}")
                print(f"Multa: R${usuario.multa:.2f}")
                print("-" * 30)
