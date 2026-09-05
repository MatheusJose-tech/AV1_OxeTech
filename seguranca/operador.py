from seguranca.logger_config import *

class seguranca_operador:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    # Função para mascarar dados sensíveis

    def mascarar_cpf(self, cpf):
        return f"{cpf[:3]}.***.***-{cpf[-2:]}"

    def mascarar_email(self, email):
        partes = email.split("@")
        if len(partes) != 2:
            return email  # Retorna o email original se não for válido

        nome_usuario, dominio = partes
        if len(nome_usuario) <= 2:
            nome_usuario_mascarado = nome_usuario[0] + "*"
        else:
            nome_usuario_mascarado = nome_usuario[0] + "*" * (len(nome_usuario) - 2) + nome_usuario[-1]

        return f"{nome_usuario_mascarado}@{dominio}"
    
    # Funções de log para diferentes níveis de severidade
    
    def mensagem_erro(self, mensagem):
        logger.error(mensagem)

    def mensagem_info(self, mensagem):
        logger.info(mensagem)

    def mensagem_debug(self, mensagem):
        logger.debug(mensagem)

    def mensagem_warning(self, mensagem):
        logger.warning(mensagem)

    def mensagem_critical(self, mensagem):
        logger.critical(mensagem)

    def mensagem_exception(self, mensagem):
        logger.exception(mensagem)

    def mensagem_log(self, mensagem):
        logger.log(logging.INFO, mensagem)

    def mensagem_log_personalizado(self, nivel, mensagem):
        logger.log(nivel, mensagem)

    