# Alert Service - CryptWatch

## 📋 Sobre o Projeto

O **Alert Service** é um microserviço desenvolvido com Clean Architecture para gerenciar alertas de preços de criptomoedas. O serviço permite criar, listar, buscar e deletar alertas que monitoram quando uma moeda atinge um determinado preço-alvo.

Este repositório faz parte do projeto **CryptWatch**, um sistema completo de monitoramento de criptomoedas. Você pode acompanhar o desenvolvimento e as tarefas no [Kanban do projeto](https://github.com/users/Emigdioriz/projects/3).

### Arquitetura

O projeto segue os princípios de Clean Architecture com as seguintes camadas:

- **Domain**: Entidades de negócio e interfaces de repositório
- **Application**: Casos de uso e DTOs
- **Infrastructure**: Implementação de repositórios e configurações de banco
- **Interfaces**: Rotas da API (FastAPI)

### Stack Tecnológica

- **Python 3.13.9**
- **FastAPI 0.121.0** - Framework web assíncrono
- **SQLAlchemy 2.0.44** - ORM com suporte async
- **PostgreSQL** - Banco de dados de produção (via asyncpg)
- **SQLite** - Banco de dados para testes (via aiosqlite)
- **Alembic 1.17.1** - Migrations de banco de dados
- **Pytest** - Framework de testes
- **UV** - Gerenciador de dependências e ambientes virtuais

---

## 🚀 Pré-requisitos

Antes de começar, você precisa ter instalado:

- **[UV](https://github.com/astral-sh/uv)** - Gerenciador de dependências Python
- **PostgreSQL** (para ambiente de produção/desenvolvimento)

### Instalação do UV

```sh
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

## 🔧 Instalação

1. Clone o repositório:
```sh
git clone https://github.com/Emigdioriz/crypto-watch-alert.git
cd crypto-watch-alert
```

2. Instale as dependências e crie o ambiente virtual:
```sh
uv sync
```

3. Configure o ambiente Python no VS Code:
   - Pressione `Cmd/Ctrl + Shift + P`
   - Selecione "Python: Select Interpreter"
   - Escolha o interpretador do `.venv`

---

## ⚙️ Configuração do Banco de Dados

### Banco de Dados de Produção/Desenvolvimento

O serviço utiliza **PostgreSQL** como banco de dados principal. Você pode configurar via Docker ou instalação local:

#### Opção 1: Docker (Recomendado)
```sh
docker run --name postgres-alert \
  -e POSTGRES_USER=alert_user \
  -e POSTGRES_PASSWORD=alert_pass \
  -e POSTGRES_DB=alert_db \
  -p 5432:5432 \
  -d postgres:16
```

#### Opção 2: PostgreSQL Local
Certifique-se de ter o PostgreSQL instalado e crie um banco de dados:
```sql
CREATE DATABASE alert_db;
CREATE USER alert_user WITH PASSWORD 'alert_pass';
GRANT ALL PRIVILEGES ON DATABASE alert_db TO alert_user;
```

### Configuração de Ambiente

O arquivo `.env` está incluído no repositório como exemplo. Configure as seguintes variáveis:

```env
# Banco de dados
DATABASE_URL=postgresql+asyncpg://alert_user:alert_pass@localhost:5432/alert_db

# Configurações da aplicação
DEBUG=True
SECRET_KEY=your-secret-key-here

# Servidor
HOST=0.0.0.0
PORT=3000
```

### Executar Migrations

Após configurar o banco de dados, execute as migrations:

```sh
# Gerar migration automaticamente (após alterar entidades)
uv run task db-automigration "nome_da_migration"

# Ou criar migration manualmente
uv run task db-migration "nome_da_migration"

# Aplicar migrations
uv run task db-migrate
```

---

## 🏃 Executando o Serviço

### Modo Desenvolvimento (com hot-reload)

```sh
uv run task dev
```

O serviço estará disponível em: `http://localhost:3000`

### Documentação da API

Acesse a documentação interativa (Swagger):
- **Swagger UI**: http://localhost:3000/docs
- **ReDoc**: http://localhost:3000/redoc

---

## 🧪 Executando os Testes

O projeto possui três tipos de testes:

### Executar todos os testes com coverage

```sh
uv run task test
```

### Executar testes específicos

```sh
# Testes unitários
uv run pytest tests/unit_test/ -v

# Testes de integração
uv run pytest tests/integration/ -v

# Testes E2E
uv run pytest tests/E2E/ -v

# Arquivo específico
uv run pytest tests/E2E/test_create_alert.py -v

# Teste específico
uv run pytest tests/E2E/test_create_alert.py::test_create_alert_success -v
```

### Coverage Report

```sh
# Gerar relatório de cobertura
uv run pytest --cov=alert --cov-report=html

# Abrir relatório no navegador
open htmlcov/index.html
```

---

## 📝 Comandos Disponíveis

O projeto utiliza **Taskipy** para facilitar tarefas comuns:

| Comando | Descrição |
|---------|-----------|
| `uv run task dev` | Inicia o servidor em modo desenvolvimento |
| `uv run task test` | Executa todos os testes com coverage |
| `uv run task lint` | Verifica código com Ruff |
| `uv run task format` | Formata código com Ruff |
| `uv run task db-automigration "msg"` | Gera migration automaticamente |
| `uv run task db-migration "msg"` | Cria migration manual |
| `uv run task db-migrate` | Aplica migrations pendentes |
| `uv run task key-generate` | Gera chave secreta para JWT |

---

## 🏗️ Estrutura do Projeto

```
crypto-watch-alert/
├── src/
│   ├── domain/               # Entidades e interfaces
│   │   ├── entities/         # Entidades de domínio (Alert)
│   │   └── interfaces/       # Contratos de repositório
│   ├── application/          # Casos de uso e DTOs
│   │   ├── use_cases/        # Lógica de negócio
│   │   └── dtos/             # Data Transfer Objects
│   ├── infraestructure/      # Implementações técnicas
│   │   ├── repositories/     # Repositórios de banco
│   │   ├── config/           # Configurações (DB, env)
│   │   └── migrations/       # Migrations Alembic
│   └── interfaces/           # Camada de API
│       └── api/
│           └── routers/      # Endpoints FastAPI
├── tests/
│   ├── unit_test/            # Testes unitários
│   ├── integration/          # Testes de integração
│   ├── E2E/                  # Testes end-to-end
│   ├── factories/            # Factories para testes
│   └── fixtures/             # Fixtures do pytest
├── pyproject.toml            # Configurações e dependências
├── alembic.ini               # Configuração do Alembic
└── README.md
```

---

## 📚 Endpoints Disponíveis

### Alertas

- **POST** `/alerts/` - Criar um novo alerta
- **GET** `/alerts/` - Listar todos os alertas
- **GET** `/alerts/{alert_id}` - Buscar alerta por ID
- **DELETE** `/alerts/{alert_id}` - Deletar um alerta

### Exemplo de Requisição

```sh
# Criar alerta
curl -X POST "http://localhost:3000/alerts/" \
  -H "Content-Type: application/json" \
  -d '{
    "symbol": "BTCUSDT",
    "targetPrice": 50000.00
  }'

# Listar alertas
curl -X GET "http://localhost:3000/alerts/"
```

---

## 🤝 Contribuindo

Este projeto faz parte do CryptWatch. Para contribuir:

1. Confira as tasks no [Kanban do projeto](https://github.com/users/Emigdioriz/projects/3)
2. Crie uma branch para sua feature
3. Siga os padrões de Clean Architecture
4. Escreva testes para novas funcionalidades
5. Execute `uv run task lint` e `uv run task format` antes de commitar
6. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT.

---

## 👨‍💻 Autor

Desenvolvido por [Emigdio Bertoldo Rizardi](https://github.com/Emigdioriz)
