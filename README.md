# Task Manager API

API profissional de gerenciamento de tarefas desenvolvida com FastAPI e MongoDB, com foco em arquitetura limpa, autenticação JWT e boas práticas de backend.

---

## Tecnologias

- Python 3.12+
- FastAPI
- MongoDB
- Motor (MongoDB Async Driver)
- JWT Authentication
- Passlib / Bcrypt
- Pydantic
- Uvicorn

---

## Funcionalidades

- CRUD de tarefas
- Autenticação com JWT
- Hash seguro de senhas
- Rotas protegidas
- Integração com MongoDB
- Documentação automática com Swagger

---

## Estrutura do Projeto

```txt
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