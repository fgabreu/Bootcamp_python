# CRUD FASTAPI POSTGRES STREAMLIT

## Backend
Nosso backend vai ser uma API, que será responsável por fazer a comunicação entre o nosso frontend com o banco de dados. Vamos detalhar cada uma das pastas e arquivos do nosso backend.

### FastAPI
O FastAPI é um framework web para construir APIs com Python. Ele é baseado no Starlette, que é um framework assíncrono para construir APIs. O FastAPI é um framework que está crescendo muito, e que tem uma curva de aprendizado muito baixa, pois ele é muito parecido com o Flask.

### Uvicorn
O Uvicorn é um servidor web assíncrono, que é baseado no ASGI, que é uma especificação para servidores web assíncronos. O Uvicorn é o servidor web recomendado pelo FastAPI, e é o servidor que vamos utilizar nesse projeto.

### SQLAlchemy
O SQLAlchemy é uma biblioteca para fazer a comunicação com o banco de dados. Ele é um ORM (Object Relational Mapper), que é uma técnica de mapeamento objeto-relacional que permite fazer a comunicação com o banco de dados utilizando objetos.

Uma das principais vantagens de trabalhar com o SQLAlchemy é que ele é compatível com vários bancos de dados, como MySQL, PostgreSQL, SQLite, Oracle, Microsoft SQL Server, Firebird, Sybase e até mesmo o Microsoft Access.

Além disso, ele realiza a sanitização dos dados, evitando ataques de SQL Injection.