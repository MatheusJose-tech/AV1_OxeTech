import datetime
from estante import banco
from livros.modelos import Livros

class Usuario:
    def __init__(self, id_usuario, nome, cpf, email, tipo):
        self.id = id_usuario
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.tipo = tipo
        self.emprestimos_ativos = 0

class Biblioteca():
    def __init__(self):
        self.usuarios = {}
        self.livros = {}
        self.emprestimos = []
    

    
        
    def adicionar_usuario(self, id_usuario, nome, cpf, email, tipo):
        novo_usuario = Usuario(id_usuario, nome, cpf, email, tipo)
        self.usuarios[id_usuario] = novo_usuario

    def adicionar_livro_na_biblioteca(self, livro):
        self.livros[livro.id] = livro
    
    def emprestar(self,id, id_livro):

        usuario = self.usuarios.get(id)
        livro = self.livros.get(id_livro)

        if usuario is None:
            print(f"Usuário com ID {id} não encontrado.")
            return   

        if livro is None:
            print(f"Livro com ID {id_livro} não encontrado.")
            return
        if livro.quantidade <= 0:
            print(f"Não há exemplares disponíveis do livro '{livro.titulo}'.")
            return

             
        tipos = banco.TIPOS
        
        if usuario.tipo in tipos:

            limite_emprestimos = tipos[usuario.tipo]

            if usuario.emprestimos_ativos < limite_emprestimos:


                livro.quantidade -= 1
                usuario.emprestimos_ativos += 1
                
                prazo = banco.prazo_por_tipo[usuario.tipo]  

                vencimento = datetime.date.today() + datetime.timedelta(days=prazo)
                vencimento_str = vencimento.strftime("%d/%m/%Y")

                self.emprestimos.append({"usuario": usuario.id, "vencimento": vencimento_str})

                print(f"Empréstimo realizado com sucesso! nome: {usuario.nome}, tipo: {usuario.tipo}, Vencimento: {vencimento}")
                print(f"Quantidade de livros restantes na estante: {livro.quantidade}")
            else:
                print("Limite de empréstimos atingido.")


# teste para ver se o limite ta funcionando

if __name__ == "__main__":
    
    biblioteca = Biblioteca()
    biblioteca.adicionar_usuario("U1", "João", "12345678900", "joao@email.com", "comum")
    biblioteca.adicionar_livro_na_biblioteca(Livros("L1", "Livro 1", "Autor 1", 5))
    biblioteca.emprestar("U1", "L1")
    biblioteca.emprestar("U1", "L1")
    biblioteca.emprestar("U1", "L1")
    biblioteca.emprestar("U1", "L1")
    biblioteca.emprestar("U1", "L1")
    print(f"Empréstimos ativos: {biblioteca.usuarios['U1'].emprestimos_ativos}")

