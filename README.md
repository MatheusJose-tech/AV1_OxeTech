# AV1_OxeTech

## 📖 Sobre o Projeto

O **AV1_OxeTech** é um sistema de gerenciamento de biblioteca desenvolvido em **Python** como parte da avaliação do curso **Treinamento de Boas Práticas para o Desenvolvimento de Softwares**, da **OxeTech**.

O projeto foi construído a partir de um **código legado**, inicialmente desenvolvido com diversos problemas de qualidade e manutenção. O objetivo da atividade foi analisar esse código, identificar os problemas existentes e aplicar técnicas de refatoração e boas práticas de desenvolvimento para tornar o sistema mais **organizado, legível, seguro, reutilizável e fácil de manter**, preservando seu comportamento original.

Durante o desenvolvimento da AV1, foram aplicados os principais conceitos abordados ao longo do módulo, incluindo:

* **Qualidade de código e Code Smells**, com melhoria de nomenclatura, remoção de números mágicos e eliminação de código duplicado;
* **Funções pequenas e responsabilidades bem definidas**, dividindo funções grandes em métodos menores e mais específicos;
* **Guard Clauses e tratamento adequado de erros**, reduzindo aninhamentos excessivos e corrigindo um bug relacionado à validação de usuários durante empréstimos;
* **Logging**, substituindo o uso excessivo de `print` por registros apropriados e evitando a exposição de dados pessoais, como CPF e e-mail;
* Aplicação dos princípios **DRY, KISS e YAGNI**, evitando duplicações e complexidades desnecessárias;
* **Princípios SOLID**, principalmente **SRP (Single Responsibility Principle)** e **OCP (Open/Closed Principle)**, separando responsabilidades e utilizando polimorfismo para facilitar a inclusão de novos tipos de usuários sem alterações generalizadas no código.

Além da refatoração estrutural, o projeto busca manter o **comportamento válido do sistema legado**, preservando funcionalidades como empréstimos, cálculo de multas e geração de relatórios. A única alteração intencional de comportamento foi a **correção do bug identificado no processo de empréstimo para usuários inexistentes**.

Dessa forma, o **AV1_OxeTech** representa a aplicação prática dos conceitos estudados no módulo, demonstrando como técnicas de boas práticas e refatoração podem transformar um código legado em uma solução mais **limpa, modular, segura e sustentável**.


## ⚙️ Funcionalidades

* **Gerenciamento de Livros:** Modelagem e estruturação dos dados dos livros (`livros/modelos.py`).
* **Controle de Acervo:** Lógica de gerenciamento da estante e comunicação com os dados (`estante/biblioteca.py` e `estante/banco.py`).
* **Segurança e Auditoria:** Gerenciamento de operadores do sistema e registro de atividades (`seguranca/operador.py` e `seguranca/logger_config.py`).
* **Geração de Relatórios:**  Exportação de relatórios pelo próprio registro de atividades (`relatorio.py`).

## 📂 Estrutura do Projeto

```text
AV1_OxeTech/
├── estante/
│   ├── __init__.py
│   ├── banco.py
│   └── biblioteca.py
├── livros/
│   ├── __init__.py
│   └── modelos.py
├── seguranca/
│   ├── __init__.py
│   ├── logger_config.py
│   └── operador.py
├── main.py
├── relatorio.py
├── relatorio.md 
├── legado.py  # codigo legado que a partir dele foi feita a refatoração 
├── log.txt
└── README.md
```

## 🚀 Como Executar

### Pré-requisitos

* [Python 3.x](https://www.python.org/) instalado na máquina.

### Execução

1. Abra o terminal e navegue até a pasta raiz do projeto:

```bash
cd AV1_OxeTech
```

2. Execute o arquivo principal (`main.py`):

```bash
python main.py
```

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Bibliotecas:** *logging*, *Datatime*
* **Arquivos de Saída:** `.txt` (`log.txt`)
