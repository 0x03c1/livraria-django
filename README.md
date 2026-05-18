# Projeto Django

Projeto Django criado para fins de estudo e prática dos conceitos fundamentais do framework.

## Arquitetura do Projeto

Um projeto Django é composto por um **módulo de configuração** (neste caso, `core/`) e uma ou mais **aplicações** independentes. Cada aplicação encapsula uma funcionalidade específica (models, views, templates, etc.) e pode ser reutilizada em outros projetos.


## Estrutura de Diretórios

```
django-ficr/
├── manage.py          # Utilitário de linha de comando do Django
├── core/              # Módulo de configuração do projeto
│   ├── __init__.py
│   ├── settings.py    # Configurações gerais (banco de dados, apps, middleware, etc.)
│   ├── urls.py        # Mapeamento de rotas raiz do projeto
│   ├── asgi.py        # Ponto de entrada para servidores ASGI
│   └── wsgi.py        # Ponto de entrada para servidores WSGI
└── requirements.txt   # Dependências do projeto
```

## Pré-requisitos

- Python 3.10+

## Primeiros Passos

### 1. Criar o ambiente virtual

O ambiente virtual isola as dependências do projeto, evitando conflitos com outros projetos Python na máquina.

```bash
python -m venv .venv
```

### 2. Ativar o ambiente virtual

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

Após a ativação, o prefixo `(.venv)` aparecerá no terminal, indicando que o ambiente está ativo.

### 3. Instalar as dependências

```bash
pip install django
```

### 4. Iniciar o servidor de desenvolvimento

```bash
python manage.py runserver
```

O servidor estará disponível em `http://127.0.0.1:8000/`.

---

### Material de apoio

Todo o conteúdo de apoio está organizado dentro da pasta [`docs/`](./docs).

| Aula | Tema                        | Link                                |
| ---- | --------------------------- | ----------------------------------- |
| 01   | Início do projeto           | [Material de Apoio](/docs/.gitkeep) |

---

## Comandos Úteis

| Comando                            | Descrição                                                                    |
| ---------------------------------- | ---------------------------------------------------------------------------- |
| `django-admin startproject core .` | Cria o projeto Django no diretório atual (o `.` evita criar uma pasta extra) |
| `python manage.py startapp <nome>` | Cria uma nova aplicação dentro do projeto                                    |
| `python manage.py makemigrations`  | Gera os arquivos de migração a partir das alterações nos models              |
| `python manage.py migrate`         | Aplica as migrações pendentes no banco de dados                              |
| `python manage.py createsuperuser` | Cria um usuário administrador para o painel `/admin`                         |
| `python manage.py runserver`       | Inicia o servidor de desenvolvimento                                         |
| `pip freeze > requirements.txt`    | Exporta as dependências instaladas para um arquivo                           |
| `pip install -r requirements.txt`  | Instala todas as dependências listadas no arquivo                            |