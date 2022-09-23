# E-commerce Arbok Team

### System

- [Python](https://www.python.org/downloads/) 3.10.4
- [Docker](https://docs.docker.com/get-docker) 20.10.18
- [Docker-compose](https://docs.docker.com/compose/install) 1.29.2

### Frameworks

- Django 4.1.1
- djongo 1.3.6
- pymongo 3.12.1
- djangorestframework 3.13.1
- django-cors-headers 3.13.0

## 🚀 Instalando

Para instalar o o projeto, siga estas etapas:

Na raíz do projeto utilize o seguinte comando para criação do virtual environment:
```
python3 -m venv venv
```

Utilize o seguinte comando para ativar o virtual environment:
```
source venv/bin/activate
```

Utilize o seguinte comando para instalar todas dependências apartir do requirements.txt:
```
pip3 install -r requirements.txt
```

## ☕ Subindo o projeto local

Para subir o projeto localmente, siga estas etapas:

- Subir o mongodb, no terminal no diretório desenv/mongodb:

```
docker-compose -f docker-compose-dev.yml up --build -d
```

- Fazer migração do dominio para o mongo no terminal da virtual env :

```
python3 manage.py makemigrations
python3 manage.py migrate
```

- Para rodar o projeto, no terminal da virtual env:

```
python3 manage.py runserver
```

Acesse [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


## 📫 GitFlow

Para contribuir com o projeto utilizando GitFlow, siga estas etapas:

1. clone este repositório.
2. Crie um branch: `git checkout -b <feature/nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push`
5. Crie a solicitação de PR.