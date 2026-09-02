import datetime
from estante import banco
from livros.modelos import Estante
class Usuario:
    def __init__(self, id_usuario, nome, cpf, email, tipo):
        self.id = id_usuario
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.tipo = tipo
        self.bloqueado = False
        self.multa = 0
        self.emprestimos_ativos = 0

class Biblioteca():
    def __init__(self):
        self.usuarios = {}
        self.livros = {}
        self.emprestimos = []
        self.estante = Estante()
        

    def mascarar_cpf(self, cpf):
            return f"{cpf[:3]}.***.***-{cpf[-2:]}"
      
    def adicionar_usuario(self, id_usuario, nome, cpf, email, tipo):

        novo_usuario = Usuario(id_usuario, nome, self.mascarar_cpf(cpf), email, tipo)
        self.usuarios[id_usuario] = novo_usuario

    def adicionar_livro_na_biblioteca(self, id_livro, titulo, autor, categoria, quantidade):

        self.estante.adicionar_livro(id_livro, titulo, autor, categoria, quantidade)
        self.livros[id_livro] = self.estante.livros[-1]  
    
    def emprestar(self,id, id_livro):

        usuario = self.usuarios.get(id)
        livro = self.livros.get(id_livro)

        if usuario.bloqueado:
            print(f"Usuário {usuario.nome} está bloqueado e não pode realizar empréstimos.")
            return
        
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

        if usuario.tipo not in tipos:
            limite_emprestimos = 1

        elif usuario.tipo in tipos:
            limite_emprestimos = tipos[usuario.tipo]

        if usuario.emprestimos_ativos < limite_emprestimos:

            if self.estante.efetivar_emprestimo(id_livro):

                    usuario.emprestimos_ativos += 1
                    prazo = banco.prazo[usuario.tipo]  

                    vencimento = datetime.date.today() + datetime.timedelta(days=prazo)
                    vencimento_str = vencimento.strftime("%d/%m/%Y")

                    self.emprestimos.append({"usuario": usuario.id, "livro": livro.id, "vencimento": vencimento_str})

                    print(f"Empréstimo realizado com sucesso!\nNome: {usuario.nome}\nCPF: {usuario.cpf}\nTipo: {usuario.tipo}\nVencimento: {vencimento_str}")
                    print(f"Quantidade de livros restantes na estante: {livro.quantidade}")
        else:
            print("Limite de empréstimos atingido.")

    def devolver(self, id_usuario, id_livro):

        usuario = self.usuarios.get(id_usuario)
        livro = self.livros.get(id_livro)

        if usuario is None:
            print(f"Usuário com ID {id_usuario} não encontrado.")
            return

        if livro is None:
            print(f"Livro com ID {id_livro} não encontrado.")
            return
        print(f"Processando devolução: usuário {usuario.nome}\nCPF: {usuario.cpf}\nlivro: {livro.titulo}\nID: {id_livro}")
        empestimo_encontrado = None

        for emprestimo in self.emprestimos:
            if emprestimo["usuario"] == id_usuario and emprestimo["livro"] == id_livro and not emprestimo.get("devolvido", False):
                empestimo_encontrado = emprestimo
                break

        if empestimo_encontrado is None:
            print(f"Não há empréstimos ativos para o usuário {usuario.nome} com o livro '{livro.titulo}'.")
            return
        
        data_hoje = datetime.date.today()
        vencimento_texto = empestimo_encontrado["vencimento"]
        vencimento_formatado = datetime.datetime.strptime(vencimento_texto, "%d/%m/%Y").date()

        if data_hoje > vencimento_formatado:

            dias_atraso = (data_hoje - vencimento_formatado).days
            print(f"Devolução atrasada em {dias_atraso} dias.")
            print(f"Aplicando multa...")

            multa = banco.MULTAS[usuario.tipo] * dias_atraso
            print(f"Valor da multa: R$ {multa:.2f}")
            print(f"Prosseguindo com a devolução do livro '{livro.titulo}'...")   

        if usuario.emprestimos_ativos > 0:

            if self.estante.efetivar_devolucao(id_livro):
        
                usuario.emprestimos_ativos -= 1
                self.emprestimos.remove(empestimo_encontrado)

                print(f"Devolução realizada com sucesso!\nNome: {usuario.nome}\nCPF: {usuario.cpf}\nTipo: {usuario.tipo}")
                print(f"Quantidade de livros restantes na estante: {livro.quantidade}")
        else:
            print("O usuário não possui empréstimos ativos para devolver.")


