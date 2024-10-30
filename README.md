# Projeto de TDD: Sistema de Leilão em Python

Este é um projeto de Test-Driven Development (TDD) que implementa um sistema de leilão em Python. A aplicação possui classes que representam o **Usuário**, **Lance** e **Leilão** e trata as exceções específicas do sistema de leilão. Este projeto foi um pequeno estudo para entender conceitos de TDD, boas práticas de código e o desenvolvimento de testes unitários em Python.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos principais:

- **dominio.py**: Contém as classes principais do sistema de leilão.
- **excecoes.py**: Define exceções específicas para tratar erros de lógica de negócios.
- **principal.py**: Executa uma simulação básica do sistema de leilão.

### Classes

1. **Classe `Usuario`**: Representa um usuário que participa de um leilão, propondo lances.
   - `nome`: Nome do usuário.
   - `carteira`: Quantidade de saldo disponível para lances.
   - `propoe_lance(leilao, valor)`: Método para propor um lance, checando se o usuário possui saldo suficiente. Caso contrário, lança a exceção `LanceInvalido`.
   
2. **Classe `Lance`**: Representa um lance em um leilão.
   - `usuario`: Usuário que fez o lance.
   - `valor`: Valor do lance proposto.
   
3. **Classe `Leilao`**: Gerencia os lances e mantém o maior e o menor lance.
   - `descricao`: Descrição do item a ser leiloado.
   - `propoe(lance)`: Método para adicionar um lance ao leilão, validando se ele é válido. Lança uma exceção `LanceInvalido` se as condições não forem atendidas.

4. **Classe `LanceInvalido`**: Exceção personalizada para tratar erros de lógica nos lances.

## Requisitos de Negócio

O projeto implementa algumas regras de negócio para garantir a integridade dos lances:
- O valor do lance deve ser menor ou igual ao valor na carteira do usuário.
- Usuários não podem propor lances consecutivos.
- O valor de um novo lance deve ser maior que o lance anterior.

## Configuração do Projeto

### Pré-requisitos

- Python 3.x


