# 📚 Bookstore (ch4-bookstore)

[![Python Version](https://img.shields.io/badge/python-3.12%20%7C%203.14-blue.svg)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/django-5.x%20%7C%206.x-green.svg)](https://www.djangoproject.com/)
[![Database](https://img.shields.io/badge/database-PostgreSQL%2015-336791.svg)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/docker-ready-2496ED.svg)](https://www.docker.com/)
[![Bootstrap](https://img.shields.io/badge/bootstrap-5.3-7952B3.svg)](https://getbootstrap.com/)

Aplicação web completa para catálogo e venda de livros desenvolvida em **Django**, estruturada com base nas melhores práticas do livro *Django for Professionals* (William S. Vincent).

O projeto conta com arquitetura modular, modelo de usuário customizado, fluxo de autenticação robusto via e-mail com `django-allauth`, banco de dados PostgreSQL containerizado no Docker, e suíte de testes automatizados.

---

## 📑 Sumário

- [Visão Geral](#-visão-geral)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Pré-requisitos](#-pré-requisitos)
- [Guia de Instalação e Execução](#-guia-de-instalação-e-execução)
  - [1. Clonar o repositório](#1-clonar-o-repositório)
  - [2. Configurar variáveis de ambiente](#2-configurar-variáveis-de-ambiente)
  - [3. Subir o banco de dados (PostgreSQL no Docker)](#3-subir-o-banco-de-dados-postgresql-no-docker)
  - [4. Instalar as dependências](#4-instalar-as-dependências)
  - [5. Executar as migrações](#5-executar-as-migrações)
  - [6. Criar um Superusuário (Admin)](#6-criar-um-superusuário-admin)
  - [7. Iniciar o servidor de desenvolvimento](#7-iniciar-o-servidor-de-desenvolvimento)
- [Execução via Docker Compose](#-execução-alternativa-via-docker-compose)
- [Variáveis de Ambiente](#-variáveis-de-ambiente)
- [Executando Testes](#-executando-testes)
- [Rotas Principais](#-rotas-principais)
- [Roadmap de Desenvolvimento](#-roadmap-de-desenvolvimento)

---

## 🌟 Visão Geral

Este projeto foi construído para servir como base sólida para uma livraria virtual moderna e segura, com ênfase em:
- **Segurança e Extensibilidade**: Substituição do modelo padrão de usuário do Django por um modelo customizado desde o primeiro commit.
- **Autenticação por E-mail**: Sistema de registro e login simplificado e seguro com `django-allauth`.
- **Isolamento de Ambiente**: Banco de dados PostgreSQL rodando em container Docker dedicado, eliminando necessidade de instalação local do SGBD.
- **Testes Abrangentes**: Testes unitários cobrindo modelos, formulários, permissões e resolução de templates e views.

---

## ✨ Funcionalidades

- [x] **Modelo de Usuário Customizado (`CustomUser`)**:
  - Estende `AbstractUser` para flexibilidade futura.
  - Painel administrativo (`admin.py`) e formulários (`forms.py`) adaptados para o novo modelo.
- [x] **Autenticação Avançada (`django-allauth`)**:
  - Autenticação e cadastro baseados em endereço de e-mail (campo username não obrigatório).
  - Verificação e confirmação de e-mail com templates customizados.
  - Envio de e-mails configurado em modo console (`console.EmailBackend`) para testes ágeis em desenvolvimento.
  - Opção de lembrar sessão do usuário (`Remember Me`).
- [x] **Interface Responsiva**:
  - Layout limpo estruturado com Bootstrap 5.
  - Integração com `django-crispy-forms` e pacote `crispy-bootstrap5` para formulários amigáveis.
  - Herança de templates com `_base.html` e suporte a arquivos estáticos (CSS, JS e imagens).
- [x] **Páginas Institucionais**:
  - Página Inicial (`home`) dinâmica de acordo com o estado da sessão (usuário anônimo vs autenticado).
  - Página Sobre (`about`).
- [x] **Suíte de Testes Automatizados**:
  - Testes de modelo para criação de usuário comum e superusuário.
  - Testes de formulário e fluxo de cadastro.
  - Testes de resolução de URL, templates e códigos de status HTTP para as páginas estáticas.

---

## 🛠 Tecnologias Utilizadas

- **Linguagem**: [Python](https://www.python.org/) (3.12+)
- **Framework Web**: [Django](https://www.djangoproject.com/)
- **Banco de Dados**: [PostgreSQL 15](https://www.postgresql.org/) via Docker
- **Gerenciador de Dependências**: [Pipenv](https://pipenv.pypa.io/)
- **Containerização**: [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/)
- **Autenticação**: [django-allauth](https://docs.allauth.org/)
- **Configurações & Variáveis**: [django-environ](https://django-environ.readthedocs.io/)
- **Estilização e Formulários**: [Bootstrap 5](https://getbootstrap.com/) & [django-crispy-forms](https://django-crispy-forms.readthedocs.io/)

---

## 📂 Estrutura do Projeto

```text
ch4-bookstore/
│
├── accounts/                  # App de autenticação e usuários
│   ├── admin.py               # Configuração do CustomUser no admin
│   ├── forms.py               # CustomUserCreationForm e CustomUserChangeForm
│   ├── models.py              # Definição do modelo CustomUser
│   ├── tests.py               # Testes de modelo e tela de cadastro
│   └── views.py               # Views de contas
│
├── pages/                     # App de páginas estáticas
│   ├── tests.py               # Testes de rotas e templates das páginas
│   ├── urls.py                # Rotas para home e about
│   └── views.py               # HomePageView e AboutPageView
│
├── django_project/            # Configuração global do projeto Django
│   ├── settings.py            # Definições de apps, auth, banco de dados e mailers
│   ├── urls.py                # Roteamento global (admin, accounts, pages, books)
│   ├── wsgi.py / asgi.py      # Entrypoints WSGI/ASGI
│
├── static/                    # Arquivos estáticos (desenvolvimento)
│   ├── css/base.css           # Estilos customizados
│   ├── js/base.js             # Scripts frontend
│   └── images/                # Imagens da aplicação
│
├── staticfiles/               # Arquivos estáticos coletados para produção
│
├── templates/                 # Templates HTML
│   ├── _base.html             # Template base com navbar e scripts
│   ├── home.html              # Página inicial
│   ├── about.html             # Página 'Sobre'
│   └── account/               # Templates customizados do allauth (login, signup, etc.)
│
├── Dockerfile                 # Definição da imagem Docker da aplicação
├── docker-compose.yml         # Orquestração do PostgreSQL e serviços
├── Pipfile / Pipfile.lock     # Dependências do projeto com versões travadas
├── .env.exemplo               # Modelo de variáveis de ambiente
└── README.md                  # Documentação do projeto
```

---

## 📋 Pré-requisitos

Antes de iniciar, certifique-se de ter instalado em sua máquina:
- [Git](https://git-scm.com/)
- [Python 3.12+](https://www.python.org/downloads/)
- [Pipenv](https://pipenv.pypa.io/en/latest/installation/) (`pip install pipenv`) ou `virtualenv`
- [Docker](https://docs.docker.com/get-docker/) e [Docker Compose](https://docs.docker.com/compose/install/)

---

## 🚀 Guia de Instalação e Execução

### 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd ch4-bookstore
```

### 2. Configurar variáveis de ambiente

Copie o arquivo de exemplo `.env.exemplo` para `.env`:

```bash
cp .env.exemplo .env
```

> Caso necessário, ajuste os valores em `.env` (a URL padrão conecta na porta `5433` mapeada pelo Docker).

### 3. Subir o banco de dados (PostgreSQL no Docker)

Inicie o serviço de banco de dados em segundo plano:

```bash
docker compose up -d db
```

Verifique se o container está saudável:
```bash
docker compose ps
```

### 4. Instalar as dependências

Utilizando o **Pipenv**:
```bash
pipenv install
pipenv shell
```

*(Opcional - Usando ambiente virtual padrão `venv`):*
```bash
python3 -m venv .venv
source .venv/bin/activate  # No Linux/macOS
# .venv\Scripts\activate   # No Windows
pip install django psycopg2-binary django-crispy-forms crispy-bootstrap5 django-allauth django-environ environs
```

### 5. Executar as migrações

Aplique as migrações para inicializar o esquema do banco de dados (incluindo tabelas do `CustomUser` e `allauth`):

```bash
python manage.py migrate
```

### 6. Criar um Superusuário (Admin)

Crie um usuário com permissões de administrador:

```bash
python manage.py createsuperuser
```

> **Nota**: O sistema utiliza autenticação por e-mail. Forneça um e-mail válido durante a criação.

### 7. Iniciar o servidor de desenvolvimento

Inicie o servidor local do Django:

```bash
python manage.py runserver
```

Abra seu navegador em [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## 🐳 Execução Alternativa via Docker Compose

Caso queira rodar tanto a aplicação web quanto o banco de dados diretamente via Docker:

1. Abra o arquivo `docker-compose.yml` e descomente o serviço `web`.
2. Execute o build e inicialize os serviços:

```bash
docker compose up --build
```

A aplicação ficará disponível em `http://127.0.0.1:8887/`.

---

## ⚙️ Variáveis de Ambiente

As configurações sensíveis são lidas a partir do arquivo `.env` na raiz do projeto:

| Variável | Descrição | Exemplo Padrão |
| :--- | :--- | :--- |
| `DATABASE_URL` | URL de conexão com o PostgreSQL | `postgres://postgres:postgres@127.0.0.1:5433/bookstore` |
| `SECRET_KEY` | Chave secreta de criptografia do Django | `secret_key` (alterar em produção) |
| `DJANGO_DEBUG` | Ativa/desativa o modo de depuração | `true` ou `false` |

---

## 🧪 Executando Testes

O projeto possui testes automatizados para verificar a integridade das regras de negócio e das rotas.

Execute todos os testes:
```bash
python manage.py test
```

Executar testes com nível de verbosidade detalhado:
```bash
python manage.py test -v 2
```

Executar testes de um aplicativo específico:
```bash
# Testes de usuários e cadastro
python manage.py test accounts

# Testes de páginas institucionais
python manage.py test pages
```

---

## 🧭 Rotas Principais

| Rota | Descrição |
| :--- | :--- |
| `/` | Página inicial (`home`) |
| `/about/` | Página informativa (`about`) |
| `/accounts/login/` | Tela de autenticação / login |
| `/accounts/signup/` | Tela de cadastro de novos usuários |
| `/accounts/logout/` | Ação de encerramento de sessão |
| `/admin/` | Painel administrativo do Django |
| `/books/` | Catálogo de livros (*em implementação*) |

---

## 🗺️ Roadmap de Desenvolvimento

- [x] Configuração inicial do projeto e Docker com PostgreSQL.
- [x] Modelo de usuário customizado (`CustomUser`).
- [x] Integração com `django-allauth` e templates customizados de autenticação.
- [x] Configuração de e-mails em ambiente de desenvolvimento.
- [x] Estilização com Bootstrap 5 e Crispy Forms.
- [ ] Implementação do app `books`:
  - [ ] Modelo `Book` (título, autor, preço, capa).
  - [ ] Listagem de livros e página de detalhes.
  - [ ] Sistema de avaliações (Reviews).
- [ ] Busca e paginação de títulos.
- [ ] Integração com Stripe para pagamentos de pedidos.
- [ ] Configuração de segurança para produção (SSL, WhiteNoise, PostgreSQL em nuvem).

---

## 📄 Licença

Este projeto é desenvolvido para fins de estudo e aprimoramento profissional com base nos conceitos do ecossistema Django. Fique à vontade para utilizá-lo como base de aprendizado.
