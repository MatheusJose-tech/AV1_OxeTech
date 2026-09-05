# Relatório de Refatoração - AV1_OxeTech

## 1. Problemas Encontrados (Categorias A-E)

* **Categoria A (SRP - Responsabilidade Única):** A classe `Sistema` atuava como "God Class", misturando persistência em memória (dicionários), regras de negócio (cálculos) e apresentação (prints).
* **Categoria B (OCP - Aberto/Fechado):** Regras de limite, prazo e multa dependiam de extensas cadeias de `if/elif` hardcoded baseadas em strings (`"comum"`, `"premium"`), dificultando a adição de novos tipos.
* **Categoria C (Bugs/Tratamento de Erros):** Acesso inseguro a chaves de dicionário no log gerava exceções fatais (`KeyError`) ao processar dados não cadastrados.
* **Categoria D (DRY - Duplicação de Código):** A verificação do tipo de usuário para aplicar regras de negócio estava duplicada tanto no método de `emprestar` quanto no de `devolver`.
* **Categoria E (Clean Code/Nomenclatura/code smell):** Uso de variáveis com nomes não descritivos (`d`, `u`, `emp`, `t`, `a`) e uso de "Magic Numbers" espalhados pelo código (7, 14, 30, limites numéricos).

---

## 2. Justificativas de Refatoração

* **Categoria A:** A separação de responsabilidades em módulos distintos (como `estante`, `livros` e `relatorio`) garantiu que cada parte do sistema tenha apenas um motivo para mudar.
* **Categoria B:** A substituição das cadeias condicionais por polimorfismo ou estratégias encapsuladas permitiu que novos perfis de usuário sejam adicionados sem modificar as lógicas centrais de empréstimo.
* **Categoria C:** A reestruturação do fluxo de validação garantiu a resiliência do sistema, impedindo que acessos prematuros quebrassem a aplicação.
* **Categoria D:** A centralização das lógicas de prazos e multas eliminou a repetição, garantindo que qualquer alteração de regra de negócio seja feita em um único lugar.
* **Categoria E:** A renomeação para variáveis descritivas (ex: de `d` para banco de livros) e a remoção de valores hardcoded transformaram o código em uma documentação viva e compreensível.

---

## 3. Análise e Correção do Bug (Parte 1-C)

**Qual era:**
Ocorria uma falha crítica (`KeyError`) caso o sistema tentasse processar um empréstimo ou devolução para um ID de usuário que não existia no banco de dados.

**Por que acontecia:**
Nos métodos `emprestar` e `devolver`, o código tentava registrar a ação imprimindo informações específicas do usuário (`self.u[id_u]["cpf"]`) *antes* de realizar a verificação condicional de segurança (`if id_u in self.u:`). Se o usuário não estivesse cadastrado, o acesso ao dicionário disparava um erro e o programa era interrompido.

**Como foi corrigido:**
A ordem de execução foi invertida. O acesso aos dados do usuário (e o respectivo print de log) foi movido para *dentro* do escopo de validação (`if id_u in self.u:`), assegurando que atributos como o CPF só sejam acessados no dicionário após a confirmação real da existência daquela chave.
