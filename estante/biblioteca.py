import datetime
from estante import banco
from livros.modelos import Estante
from seguranca.operador import seguranca_operador
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
        self.operador = seguranca_operador()
        

      
    def adicionar_usuario(self, id_usuario, nome, cpf, email, tipo):

        novo_usuario = Usuario(id_usuario, nome, self.operador.mascarar_cpf(cpf), self.operador.mascarar_email(email), tipo)
        self.usuarios[id_usuario] = novo_usuario

    def adicionar_livro_na_biblioteca(self, id_livro, titulo, autor, categoria, quantidade):

        self.estante.adicionar_livro(id_livro, titulo, autor, categoria, quantidade)
        self.livros[id_livro] = self.estante.livros[-1]  
    
    def emprestar(self,id, id_livro):

        usuario = self.usuarios.get(id)
        livro = self.livros.get(id_livro)

        if usuario.bloqueado:
            return self.operador.mensagem_warning(f"Usuário {usuario.nome} está bloqueado e não pode realizar empréstimos.")
            
        
        if usuario is None:
            return self.operador.mensagem_erro(f"Usuário com ID {id} não encontrado.")
            

        if livro is None:
            return self.operador.mensagem_erro(f"Livro com ID {id_livro} não encontrado.")

        if livro.quantidade <= 0:
            return self.operador.mensagem_info(f"Não há exemplares disponíveis do livro '{livro.titulo}'.")
            

             
        tipos = banco.TIPOS

        if usuario.tipo not in tipos:
            limite_emprestimos = 1

        elif usuario.tipo in tipos:
            limite_emprestimos = tipos[usuario.tipo]

        if usuario.emprestimos_ativos < limite_emprestimos:

            if self.estante.efetivar_emprestimo(id_livro):

                    usuario.emprestimos_ativos += 1
                    prazo = banco.PRAZO[usuario.tipo]  

                    vencimento = datetime.date.today() + datetime.timedelta(days=prazo)
                    vencimento_str = vencimento.strftime("%d/%m/%Y")

                    self.emprestimos.append({"usuario": usuario.id, "livro": livro.id, "vencimento": vencimento_str})

                    self.operador.mensagem_info(f"Empréstimo realizado com sucesso!\nNome: {usuario.nome}\nCPF: {usuario.cpf}\nTipo: {usuario.tipo}\nVencimento: {vencimento_str}")
                    self.operador.mensagem_info(f"Quantidade de livros restantes na estante: {livro.quantidade}")
        else:
            self.operador.mensagem_warning("Limite de empréstimos atingido.")

    def devolver(self, id_usuario, id_livro):

        usuario = self.usuarios.get(id_usuario)
        livro = self.livros.get(id_livro)

        if usuario is None:
            self.operador.mensagem_erro(f"Usuário com ID {id_usuario} não encontrado.")
            return

        if livro is None:
            self.operador.mensagem_erro(f"Livro com ID {id_livro} não encontrado.")
            return

        self.operador.mensagem_info(f"Processando devolução: usuário {usuario.nome}\nCPF: {usuario.cpf}\nlivro: {livro.titulo}\nID: {id_livro}")
        empestimo_encontrado = None

        for emprestimo in self.emprestimos:
            if emprestimo["usuario"] == id_usuario and emprestimo["livro"] == id_livro and not emprestimo.get("devolvido", False):
                empestimo_encontrado = emprestimo
                break

        if empestimo_encontrado is None:
            self.operador.mensagem_erro(f"Não há empréstimos ativos para o usuário {usuario.nome} com o livro '{livro.titulo}'.")
            return
        
        data_hoje = datetime.date.today()
        vencimento_texto = empestimo_encontrado["vencimento"]
        vencimento_formatado = datetime.datetime.strptime(vencimento_texto, "%d/%m/%Y").date()

        if data_hoje > vencimento_formatado:

            dias_atraso = (data_hoje - vencimento_formatado).days
            self.operador.mensagem_warning(f"Devolução atrasada em {dias_atraso} dias.")
            self.operador.mensagem_info(f"Aplicando multa...")

            multa = banco.MULTAS[usuario.tipo] * dias_atraso
            self.operador.mensagem_info(f"Valor da multa: R$ {multa:.2f}")
            self.operador.mensagem_info(f"Prosseguindo com a devolução do livro '{livro.titulo}'...")   

        if usuario.emprestimos_ativos > 0:

            if self.estante.efetivar_devolucao(id_livro):
        
                usuario.emprestimos_ativos -= 1
                self.emprestimos.remove(empestimo_encontrado)
                self.emprestimos.append({"usuario": usuario.id, "livro": livro.id, "vencimento": empestimo_encontrado["vencimento"], "devolvido": True})

                self.operador.mensagem_info(f"Devolução realizada com sucesso!\nNome: {usuario.nome}\nCPF: {usuario.cpf}\nTipo: {usuario.tipo}")
                
                self.operador.mensagem_info(f"Quantidade de livros restantes na estante: {livro.quantidade}")
        else:
            self.operador.mensagem_info("O usuário não possui empréstimos ativos para devolver.")


    def reservar_livro(self, id_usuario, id_livro):

        usuario = self.usuarios.get(id_usuario)
        livro = self.livros.get(id_livro)

        if usuario is None:
            self.operador.mensagem_erro(f"Usuário com ID {id_usuario} não encontrado.")
            return

        if livro is None:
            self.operador.mensagem_erro(f"Livro com ID {id_livro} não encontrado.")
            return

        if livro.quantidade == 0:
            self.operador.mensagem_info(f"Livro '{livro.titulo}' está esgotado. Processando reserva para o usuário {usuario.nome}...")
            self.operador.mensagem_info(f"Reserva do livro '{livro.titulo}' realizada com sucesso para o usuário {usuario.nome}.")
        else:
            self.operador.mensagem_info(f"Livro '{livro.titulo}' está disponível. Nenhuma reserva necessária.")
            

        



            