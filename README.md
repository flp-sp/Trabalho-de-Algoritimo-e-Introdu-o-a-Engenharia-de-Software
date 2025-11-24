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
### Caso de Teste 1 – Cadastro válido
| Item | Valor |
|------|--------|
| **Entrada** | Nome: “Ana Silva”, Email: “ana@dominio.com”, Idade: 25 |
| **Resultado Esperado** | Dados aceitos e armazenados na lista/dicionário. Nenhuma mensagem de erro. |

---

### Caso de Teste 2 – Nome inválido
| Item | Valor |
|------|--------|
| **Entrada** | Nome: “Jo”, Email: “joao@dominio.com”, Idade: 30 |
| **Resultado Esperado** | Erro: “Nome deve ter mais de 2 caracteres.” <br> Solicitar nova entrada. |

---

### Caso de Teste 3 – Email inválido
| Item | Valor |
|------|--------|
| **Entrada** | Nome: “Carlos”, Email: “carlosgmail.com”, Idade: 22 |
| **Resultado Esperado** | Erro: “E-mail inválido. Deve conter ‘@dominio’.” <br> Solicitar nova entrada. |

---

### Caso de Teste 4 – Idade inválida
| Item | Valor |
|------|--------|
| **Entrada** | Nome: “Marina”, Email: “marina@dominio.com”, Idade: -5 |
| **Resultado Esperado** | Erro: “Idade deve ser maior que 0.” <br> Solicitar nova entrada. |

---

### Caso de Teste 5 – 5 cadastros completos
| Item | Valor |
|------|--------|
| **Entrada** | Cinco usuários válidos cadastrados |
| **Resultado Esperado** | Exibir lista final com os 5 usuários armazenados corretamente. |

---

### Caso de Teste 6 – Exibição dos dados
```
Usuário 1: Ana Silva, ana@dominio.com, 25
Usuário 2: João Pedro, joao@dominio.com, 19
Usuário 3: Pedro André, pedro@dominio.com, 25
Usuário 4: João Carlos, carlos@dominio.com, 27
Usuário 5: Monica Silva, monica@dominio.com, 43
```