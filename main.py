from estante.biblioteca import Biblioteca
from livros.modelos import Estante
import datetime
from relatorio import Relatorio

if __name__ == "__main__":
    biblioteca = Biblioteca()
     
        # --- Cadastro de livros ---
    biblioteca.adicionar_livro_na_biblioteca("L1", "Clean Code", "Robert Martin", "tecnico", 2)
    biblioteca.adicionar_livro_na_biblioteca("L2", "O Hobbit", "Tolkien", "ficcao", 1)
    biblioteca.adicionar_livro_na_biblioteca("L3", "SICP", "Abelson", "tecnico", 3)
     
    # --- Cadastro de usuarios (um de cada tipo) ---
    biblioteca.adicionar_usuario("U1", "Ana", "11122233344", "ana@email.com", "comum")
    biblioteca.adicionar_usuario("U2", "Bruno", "55566677788", "bruno@email.com", "premium")
    biblioteca.adicionar_usuario("U3", "Carla", "99988877766", "carla@email.com", "funcionario")
     
    print("========== CENARIO 1: emprestimos normais ==========")
    biblioteca.emprestar("U1", "L1")   # comum pega tecnico -> prazo 7 dias
    biblioteca.emprestar("U2", "L2")   # premium pega ficcao -> prazo 14 dias
    biblioteca.emprestar("U3", "L3")   # funcionario pega tecnico -> prazo 30 dias
     
    print()
    print("========== CENARIO 2: livro esgotado ==========")
    # L2 so tinha 1 exemplar, ja emprestado para U2
    biblioteca.emprestar("U1", "L2")   # deve falhar: indisponivel
     
    print()
    print("========== CENARIO 3: limite de emprestimos (comum = 3) ==========")
        # Ana (comum) ja tem L1. Vamos testar o limite.
    biblioteca.adicionar_livro_na_biblioteca("L4", "Livro Extra 1", "Autor", "geral", 5)
    biblioteca.adicionar_livro_na_biblioteca("L5", "Livro Extra 2", "Autor", "geral", 5)
    biblioteca.adicionar_livro_na_biblioteca("L6", "Livro Extra 3", "Autor", "geral", 5)
    biblioteca.emprestar("U1", "L4")   # 2o emprestimo de Ana -> OK
    biblioteca.emprestar("U1", "L5")   # 3o emprestimo de Ana -> OK
    biblioteca.emprestar("U1", "L6")   # 4o emprestimo -> deve falhar (limite 3)
     
    print()
    print("========== CENARIO 4: devolucao no prazo (sem multa) ==========")
    biblioteca.devolver("U1", "L1")    # devolvido no prazo -> multa 0
     
    print()

    print("========== CENARIO 5: devolucao com ATRASO e multa por tipo ==========")
    # Para demonstrar multa, forcamos o vencimento de alguns emprestimos para o passado.
    # (Na pratica isso aconteceria com o tempo, aqui será apenas uma simulação)
    import datetime as data
     
    # Ana (comum): multa de 2/dia. Atraso de 5 dias -> multa 10
    for usuario in biblioteca.emprestimos:

        if usuario.get("usuario") == "U1" and usuario.get("livro") == "L4":
            data_atrasada = data.date.today() - data.timedelta(days=5)
            usuario["vencimento"] = data_atrasada.strftime("%d/%m/%Y")
    print()
    print("Devolvendo livro L4 para usuário U1 (Ana) com atraso de 5 dias...")   
    print()
    biblioteca.devolver("U1", "L4")    # esperado: multa 10
     
        # Bruno (premium): multa de 1/dia. Atraso de 10 dias -> multa 10
    print()
    print("Devolvendo livro L2 para usuário U2 (Bruno) com atraso de 10 dias...")
    print()

    for usuario in biblioteca.emprestimos:
        if usuario.get("usuario") == "U2" and usuario.get("livro") == "L2":
            data_atrasada = data.date.today() - data.timedelta(days=10)
            usuario["vencimento"] = data_atrasada.strftime("%d/%m/%Y")
        biblioteca.devolver("U2", "L2")    # esperado: multa 10
     
        # Carla (funcionario): multa 0/dia. Mesmo com atraso -> multa 0
    print()
    print("Devolvendo livro L3 para usuário U3 (Carla) com atraso de 20 dias...")
    print()

    for usuario in biblioteca.emprestimos:
        if usuario.get("usuario") == "U3" and usuario.get("livro") == "L3":
            data_atrasada = data.date.today() - data.timedelta(days=20)
            usuario["vencimento"] = data_atrasada.strftime("%d/%m/%Y")
        biblioteca.devolver("U3", "L3")    # esperado: multa 0 (funcionario nao paga)
    print()

    print("========== CENARIO 6: relatorio final ==========")
    relatorio = Relatorio(biblioteca)
    relatorio.gerar_relatorio()
    relatorio.gerar_relatorio_resumido()
