# Especificação de Requisitos

## 1. Introdução
Registrar os requisitos de um sistema de Cadastro de Projetos

## 2. Visão Geral do Sistema
Sistema para uso interno com o objetivo de receber propostas de projetos de clientes externos com a finalidade de usá-los como projetos de extensão para os alunos do IBMEC.

## 3. Requisitos Funcionais

#### RF01 – O sistema deve permitir o cadastro entre dois perfil de usuário: Coordenador e cliente
#### RF02 – O sistema deve permitir que o cliente faça o cadastro de projetos
#### RF03 - O sistema deve exibir os projetos enviados, além de exibir status indicando se está em análise ou foi aprovado
#### RF04 - O sistema deve permitir que coordenadores criem contas para professores
#### RF05 - O sistema deve permitir que os professores criem grupos e alunos
#### RF06 - O sistema deve permitir que coordenadores atribuam professores a projetos que foram aprovados
#### RF07 - O sistema deve exibir projetos que já foram concluídos e informações sobre ele, como a tecnologia utilizada e o cliente
#### RF08 - O sistema deve permitir que professores atribuam grupos aos projetos que ele possui

## 4. Requisitos Não Funcionais

#### RNF01 – Segurança
Cada usuário deve acessar somente funcionalidades que o seu perfil permite

#### RNF02 – Desempenho
O envio de projetos deve ser realizado em menos de 5 segundos

#### RNF03 – Usabilidade
O sistema deve ser fácil de usar, mesmo sem treinamento
Mensagens de erro e instruções devem ser claras

#### RNF04 – Manutenibilidade
O sistema deve ser organizado de forma que futuras alterações possam ser feitas sem complicações.

## 5. Regras de Negócio

#### RN01 - Validação de Dados de Cadastro
O sistema deve garantir que o e-mail informado pelo usuário seja único e válido, impedindo o cadastro de contas duplicadas ou com e-mails inválidos.

#### RN02 - Recuperação de Senha
O sistema deve permitir que o usuário solicite a recuperação de senha por meio do e-mail cadastrado, enviando um link seguro para redefinição da senha.

#### RN03 - Perfil de Acesso
Usuários cadastrados devem ser atribuídos a perfis de acesso (coordenador, usuário comum, professor) conforme regras definidas pela organização, limitando funcionalidades disponíveis conforme o perfil.

#### RN04 - Cadastro de projetos
Projetos só podem ser inseridos na plataforma com todos os campos preenchidos.

## 6. Interfaces Externas
Descreve integrações com outros sistemas, APIs, hardware ou bancos de dados.

## 7. Restrições
Lista limitações técnicas, legais ou de negócio.

## 8. Critérios de Aceitação
Define condições para validação dos requisitos e aceitação do sistema.

## 9. Glossário
Explica termos técnicos ou específicos do domínio.

## 10. Referências
Relaciona documentos, normas e materiais utilizados.