# Especificação de Requisitos

## 1. Introdução
Registrar os requisitos de um sistema de recebimento de propostas de projetos de extesão.

## 2. Visão Geral do Sistema
Sistema para uso interno com o objetivo de receber propostas de projetos de clientes externos com a finalidade de usá-los como projetos de extensão para os alunos do IBMEC.

## 3. Requisitos Funcionais

- **RF01** – O sistema deve permitir o login e cadastro de usuários.
- **RF02** – O sistema deve permitir que o cliente envie propostas de projetos de extensão.
- **RF03** - O sistema deve exibir as propostas enviadas e status de andamento.
- **RF04** - O sistema deve permitir que coordenadores criem contas para professores.
- **RF05** - O sistema deve permitir que os professores anotem grupos responsáveis para cada um de seus projetos.
- **RF06** - O sistema deve permitir que coordenadores relacionem professores a projetos.
- **RF07** - O sistema deve exibir projetos concluídos e informações sobre ele, como a tecnologia utilizada e o cliente.
- **RF08** - O sistema deve permitir que professores atribuam grupos aos projetos que ele possui.
- **RF09** – O sistema deve permitir que coodenadores aceitem ou recusem propostas.


## 4. Requisitos Não Funcionais

#### Segurança
- Cada usuário deve acessar somente funcionalidades que o seu perfil permite

#### Desempenho
- O envio de projetos deve ser realizado em menos de 5 segundos

#### Usabilidade
- O sistema deve ser fácil de usar, mesmo sem treinamento
- Mensagens de erro e instruções devem ser claras

#### Manutenibilidade
- O sistema deve ser organizado de forma que futuras alterações possam ser feitas sem complicações.

## 5. Regras de Negócio

### Login e Cadastro:
- Apenas usuários registrados podem acessar a plataforma.
- Sistemas de validação para email e contato devem ser implementados para garantir que apenas emails e contatos válidos sejam utilizados.

### Perfis e Permissões de Usuário:
- Clientes externos podem enviar, alterar e excluir propostas.
- Coordenadores tem total acesso ao sistema, incluindo recusar e editar propostas, criar conta de professores, relacionar professores a projetos, gerenciar projetos (editar, excluir, tranformar novamente em proposta, marcar como concluido).
- Professores anotam grupos de alunos a seus respectivos projetos.

### Regras para Propostas:
**Envio de propostas:**  

- Somente propostas com todos os campos obrigatórios preenchidos poderão ser enviadas.
- Cada cliente terá um limite de até 5 propostas por categoria para evitar excesso de propostas.
- Cada proposta só podera fazer parte de uma categoria, sendo necessário reenvia-la em categorias diferentes conforme a necessidade.

**Gerenciamento de Propostas:**  

- Coordenadores podem optar por inserir observações nas propostas antes de aceitá-las.

### Regras para Projetos:
- Clientes poderão solicitar alteração de projetos aprovados.
- Alterações em projetos só serão realizadas conforme permissão do Coordenador.
- Projetos só poderão ser transformados em proposta com justificativa.

### Notificações e Feedback

**Notificações:**  

- Sempre que uma proposta for aprovada o cliente deverá ser notificado.
- Coordenadores deverão receber notificação automática para projetos que ainda não tem professores.
- Coordenadores e professores (somente de seus projetos) deverão receber notificação de urgência para projetos cujo tempo de entrega esteja próximo e o status não esteja como concluído.
- Clientes serão notificados sempre que um projeto seu for concluído.  

**Feedback:**  

- Clientes podem avaliar seus projetos concluídos com comentário
