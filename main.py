from estante.biblioteca import Biblioteca
from livros.modelos import Livros

if __name__ == "__main__":
    # 1. Inicializa o sistema da biblioteca
    biblioteca = Biblioteca()
    
    # 2. Cadastra o usuário João
    biblioteca.adicionar_usuario("U1", "João", "12345678900", "joao@email.com", "comum")
    biblioteca.adicionar_usuario("U2", "Maria", "98765432100", "maria@email.com", "premium")
    biblioteca.adicionar_usuario("U3", "Carlos", "45678912300", "carlos@email.com", "funcionario")
    
    # 3. Cria um livro usando a classe do módulo livros
    livro_teste = Livros("L1", "O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia", 3)
    
    # 4. Entrega o livro para a biblioteca observar e guardar
    biblioteca.adicionar_livro_na_biblioteca(livro_teste)
    
    print(f"--- Estoque inicial do livro: {livro_teste.quantidade} ---\n")
    
    # 5. Executa os empréstimos sequenciais para testar as validações
    biblioteca.emprestar("U1", "L1")  # 1º Empréstimo
    biblioteca.emprestar("U2", "L1")  # 2º Empréstimo
    biblioteca.emprestar("U3", "L1")  # 3º Empréstimo (Estoque zera aqui)
    biblioteca.emprestar("U1", "L1")
    biblioteca.emprestar("U3", "L1")  # 4º Empréstimo (Deve barrar por falta de estoque)
    
    # 6. Exibe o resultado final no perfil do usuário
    usuario_joao = biblioteca.usuarios["U1"]
    print(f"Empréstimos ativos finais do João: {usuario_joao.emprestimos_ativos}")
    usuario_maria = biblioteca.usuarios["U2"]
    print(f"Empréstimos ativos finais da Maria: {usuario_maria.emprestimos_ativos}")
    usuario_carlos = biblioteca.usuarios["U3"]
    print(f"Empréstimos ativos finais do Carlos: {usuario_carlos.emprestimos_ativos}")
    print(f"Estoque do livro {livro_teste.titulo}: {livro_teste.quantidade}")