# mongodb

## System

* [Docker](https://docs.docker.com/get-docker) : 20.10.18
* [Docker-compose](https://docs.docker.com/compose/install) : 1.29.2

## Setup


#### 1. Configurando mongodb

Rode os seguintes comandos para subir o compose de desenvolvimento:
```sh
$ docker-compose -f -docker-compose-dev.yml up --build -d
```

### Mongo Express

Abra [https://localhost:8081](https://localhost:8081)


## Comandos Docker-compose

| Command | Description |
| ------ | ------ |
| docker-compose up -d | Create a new container in the background (-d) |
| docker-compose down | Remove an existing container |
| docker-compose start | Start an existing container |
| docker-compose stop | Pause an existing container |
