# Projeto de Software Simples com Documentação e Codificação em C ou Python
---
## Descrição do problema
Dificuldade de armazenamento e consulta de dados de usúarios de forma prática e organizada.
---
## Requisitos funcionais
Número | Requisito
------ | ---------
RF01 | O sistema deve pedir os dados do usuário (nome, e-mail, idade).
RF02 | O sistema deve validar se os dados inseridos são válidos(Idade maior que 0, e-mail contendo “@dominio”, nome maior que dois caracteres).
RF03 | O sistema deve armazenar os dados do usuário em um dict ou lista(a definir).
RF04 | O sistema deve repetir o processo com 5 usuários.
RF05 | O sistema deve exibir os dados cadastrados.

---
## Fluxograma
1. Entrada de dados do usuário
2. Validação dos dados do usuário
    1. Se idade maior que 0, e-mail contendo “@dominio” e nome maior que dois caracteres o sistema prossegue
    2. Senão o sistema pede que o usuário tente novamente cadastrar um usuário
3. Repete para 5 usuários
4. Mostra os dados dos usuários cadastrados
---
## Plano de testes
