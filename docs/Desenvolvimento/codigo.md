# Explicação Geral do Código (models.py e forms.py)

Este documento visa explicar de forma enxuta e resumida como funcionam os **modelos** e os **formulários** no sistema e também dando uma breve explicação da lógica por trás do código.  
O projeto utiliza **Python**, **Django** e o ORM do Django para gerenciar banco de dados, validações e criação de usuários.

---

# Linguagens e Tecnologias
- Python  
- Django  
- Django ModelForm  
- Django ORM  

---

# MODELS.py — Estrutura do Banco de Dados

Esse arquivo define as **tabelas**, **campos** e **relacionamentos** usados no sistema.

## Proposta
Representa uma proposta de projeto enviada por uma empresa.

Principais informações:
- Nome da solução  
- Objetivo e tecnologias  
- Dados de contato  
- Tipo de sistema  
- Experiência e disponibilidade  
- Empresa responsável  
- Situação da proposta  

Relacionamento:
- `empresa` → conecta a proposta à empresa que a enviou.

---

## Projeto
Representa um projeto oficial do sistema.

Contém:
- Nome, descrição e status  
- Datas de início e fim  
- Coordenador responsável  
- Professor envolvido  
- Proposta de origem  
- Grupo de alunos  

Serve para acompanhar oficializar o desenvolvimento um projeto a partir de uma proposta. 
---

## Coordenador
Usuário com privilégios de admin no sistema, podendo recusar ou aprovar propostas, e transforma-las em projetos. Também pode atribuir professores a projetos aprovados.
- Matrícula  
- Email  
- Telefone  

Possui validações como tamanho mínimo da matrícula e formato do telefone.

---

## Professor
Usuário comum do sistema,com privilégios normais.
- Nome  
- Matrícula  
- Email  

Utilizado para vincular professores a projetos.

---

## Empresa
Usuário comum do sistema, com privilégios normais.
função: empresa pode criar propostas e propor ao coordenador(admin), que então pode aceitar ou rejeitar propostas, e caso aprovadas, atribuir elas a professores.
Campos:
- Nome da empresa  
- CNPJ  
- Endereço  
- Email e telefone  
- Observações  
- `usuario` → ligação com um usuário Django (login)

Relacionamento importante:
- Uma empresa pode ter várias propostas (`empresa.propostas.all()`).

---

# FORMS — Validação de Dados

Os formulários recebem dados enviados pelos usuários e validam antes de salvar no banco.

---

## Objetivo Geral dos Formulários
- receber dados enviados via tela  
- validar antes de salvar  
- verificar senhas  
- impedir dados inconsistentes  
- criar objetos prontos para serem salvos  

---

## CadastroForm
Usado para criar um **usuário do Django**.

Funções:
- validar username, email e senha  
- confirmar senha  
- garantir que o usuário não exista  
- exigir senha forte  

A senha real é salva usando `create_user()` na view.

---

## EmpresaForm
Usado para cadastrar uma **Empresa(usuário comum)**.

Valida:
- nome da empresa  
- CNPJ  
- contato e telefone  
- senha + confirmação  

Após a validação:
- a view cria um usuário Django  
- a empresa é vinculada a esse usuário  

---

## ProfessorForm
Usado para cadastrar um **Professor(usuário comum)**.

Valida:
- nome  
- matrícula  
- email  
- senha + confirmação  



## CoordenadorForm
Usado para cadastrar um **Coordenador(usuário admin)**

Valida:
- nome  
- matrícula  
- email  
- telefone  
- senha + confirmação  



## PropostaForm
Usado para cadastrar uma **Proposta**.

Funções:
- validar os campos preenchidos  
- salvar direto no banco  
- não envolve senha  

Serve para registrar propostas enviadas pelas empresas.

---

# RESUMO FINAL

## Models
- Definem a estrutura do banco.  
- Conectam empresas, propostas, projetos, professores e coordenadores.  
- Possuem validações como CNPJ, telefone e matrículas.  
- Usam relacionamentos (`ForeignKey`, `OneToOne`).

## Forms
- Garantem que os dados enviados sejam válidos.  
- Formularios com senha exigem confirmação.  
- A criação do usuário Django é feita nas views.  
- PropostaForm apenas salva os dados da proposta.

Este documento resume o funcionamento essencial do backend referente aos arquivos `models.py` e `forms.py`.
