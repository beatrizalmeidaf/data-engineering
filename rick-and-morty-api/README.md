# Rick e Morty Project ⚗️

## Introdução à API e Uso da Biblioteca Requests
Uma API (Interface de Programação de Aplicações) serve como um meio de comunicação entre diferentes programas, permitindo a troca de dados e funcionalidades. Neste projeto, utilizamos a API do Rick and Morty, que fornece informações detalhadas sobre personagens, locais e episódios. Para acessar esses dados, empregamos a biblioteca `requests`, que realiza requisições HTTP à API e retorna os dados em formato estruturado.

## Formato de Retorno da API
A resposta da API é fornecida em JSON (JavaScript Object Notation), um formato leve e amplamente utilizado para transmissão de dados. O JSON é estruturado de maneira semelhante a um dicionário no Python, podendo incluir listas e outros dicionários aninhados, o que facilita sua manipulação em códigos Python.

---

## Estrutura do Projeto
Este projeto demonstra como uma ideia simples pode evoluir para um projeto de portfólio robusto na área de Engenharia de Dados. A seguir, descreve-se as etapas principais:

### Etapa 1: Trabalhando com APIs
1. **Selecionar uma API Pública:** Identificar uma API relevante para o objetivo do projeto.
2. **Extração de Dados:** Desenvolver um script em Python para realizar a extração dos dados e transformá-los em um DataFrame utilizando a biblioteca `pandas`.
3. **Salvamento de Dados:** Implementar a funcionalidade de salvar os dados extraídos em diferentes formatos, como:
   - `.csv`
   - `.xlsx`
   - `.parquet`

### Etapa 2: Integração com Bancos de Dados
4. **Configuração do DBeaver:** Instalar o DBeaver para gerenciar e interagir com bancos de dados.
5. **Criação de Bancos de Dados:** Configurar três bancos de dados locais: Oracle, MySQL e PostgreSQL.
6. **Envio de Dados:** Adaptar o código para salvar os dados diretamente em cada banco de dados utilizando bibliotecas específicas, como `cx_Oracle`, `mysql-connector-python`, entre outras.

### Etapa 3: Explorando Computação em Nuvem
7. **Armazenamento no AWS S3:** Refazer o salvamento de dados enviando os arquivos para um bucket no AWS S3.
8. **Banco de Dados na Nuvem:** Configurar bancos de dados na AWS RDS e ajuste o código para enviar os dados para esses bancos.

### Etapa 4: Implementando Infraestrutura como Código (IaC)
9. **Automatização com Terraform:** Substituir o processo manual de criação dos bancos de dados na nuvem por scripts em Terraform, garantindo maior escalabilidade e reproducibilidade.

---

## Competências Desenvolvidas
Este projeto proporciona experiências práticas em diversas áreas fundamentais da Engenharia de Dados:

- **Linguagem Python:** Desenvolvimento de scripts para manipulação de dados e interação com APIs.
- **DataFrames:** Uso da biblioteca `pandas` para organização e análise de dados.
- **Gestão de Bancos de Dados:** Configuração e manipulação de bancos de dados relacionais (Oracle, MySQL, PostgreSQL).
- **Armazenamento em Arquivos:** Salvamento de dados nos formatos `.csv`, `.xlsx` e `.parquet`.
- **SQL:** Criação e consulta de dados em bancos relacionais.
- **Serviços em Nuvem:** Interação com AWS S3 e RDS.
- **Infraestrutura como Código:** Automatização de infraestrutura com Terraform.
