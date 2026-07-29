# 📋 Sistema de Cadastro de Pessoas 

Projeto desenvolvido em Python para simular um sistema simples de cadastro de pessoas com persistência de dados em arquivo de texto (`.txt`).

## 🚀 Funcionalidades

- **Verificação de Arquivo:** Checa automaticamente se o banco de dados (`cadastro.txt`) existe e o cria se necessário.
- **Visualização de Cadastros:** Leitura e exibição formatada dos dados gravados.
- **Novo Cadastro:** Entrada de dados tratada (validação de nome e idade) com salvamento no arquivo.
- **Menu Interativo:** Interface via terminal amigável e com validação de opções.

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Módulo `time`** (nativo do Python)
- **Manipulação de Arquivos e Módulos/Pacotes customizados**

## 📂 Estrutura do Projeto

```text
├── main.py                  # Módulo principal (execução do programa)
├── cadastro.txt             # Arquivo onde os dados são salvos
└── Cadastro/                # Pacote de módulos do sistema
    └── ficha/
        ├── interface.py     # Funções de layout e leitura de números
        ├── telaconsulta.py  # Funções de manipulação do arquivo .txt
        └── telacadastro.py  # Funções para validação e cadastro

## 💻 Prévia do Sistema

```text
==============================
        MENU PRINCIPAL        
==============================
1 - Ver pessoas cadastradas
2 - Cadastrar nova pessoa
3 - Sair do Sistema
==============================
Sua Opção: 1

------------------------------
      PESSOAS CADASTRADAS     
------------------------------
Ana Paula           32 anos
Carlos Eduardo      28 anos

---

👨‍💻 **Sobre o desenvolvedor**
Projeto criado por um aspirante a desenvolvedor Python, com foco em evolução contínua, boas práticas e construção de portfólio.

---

🧑‍💻 Alexandre Dias Garcia 🔗 https://www.linkedin.com/in/alexandred-garcia

📧 alexandredgarcia23@gmail.com
   
