API profissional de gerenciamento de tarefas desenvolvida com FastAPI
 e MongoDB
, com foco em arquitetura limpa, autenticação JWT e boas práticas de backend.

Tecnologias
Python 3.12+
FastAPI
MongoDB
Motor (MongoDB Async Driver)
JWT Authentication
Passlib/Bcrypt
Pydantic
Uvicorn
Funcionalidades
CRUD de tarefas
Autenticação com JWT
Hash seguro de senhas
Rotas protegidas
Integração com MongoDB
Documentação automática com Swagger
Estrutura do Projeto
app
├── core
│   ├── config.py
│   └── security.py
├── database
│   └── database.py
├── models
│   └── user.py
├── routes
│   ├── auth.py
│   └── tasks.py
├── main.py
Configuração do Ambiente

Crie o ambiente virtual:

python -m venv .venv

Ative o ambiente virtual:

Windows
.\.venv\Scripts\Activate.ps1
Linux/macOS
source .venv/bin/activate

Instale as dependências:

pip install -r requirements.txt
Variáveis de Ambiente

Crie um arquivo .env na raiz do projeto:

PROJECT_NAME=Task Manager API
API_V1_STR=/api/v1

MONGODB_URL=your_mongodb_connection
DATABASE_NAME=task_manager

SECRET_KEY=your_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=60
ALGORITHM=HS256
Executando o Projeto
uvicorn app.main:app --reload

Servidor disponível em:

http://127.0.0.1:8000
Documentação da API

Swagger/OpenAPI:

http://127.0.0.1:8000/docs

ReDoc:

http://127.0.0.1:8000/redoc
Autenticação

A API utiliza autenticação JWT via header:

Authorization: Bearer <token>
Status do Projeto

Em desenvolvimento.

