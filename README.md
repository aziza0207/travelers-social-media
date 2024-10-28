## Локальный запуск приложения через docker-compose

Наберите команду в терминале

```shell
 docker compose up --build

```
Создайте файл .env

```shell
SECRET_KEY=my_secret
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=hello_django
SQL_USER=hello_django
SQL_PASSWORD=hello_django
SQL_HOST=db
SQL_PORT=5432
```
и env.db 

```shell
POSTGRES_USER=hello_django
POSTGRES_PASSWORD=hello_django
POSTGRES_DB=hello_django

```

### После разворота

Swagger - http://0.0.0.0:8000/api/docs/

Admin - http://0.0.0.0:8000/admin/

## Локальный запуск приложения через docker-compose

Создайте файл .env


```shell
SECRET_KEY=my_secret
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=
SQL_USER=
SQL_PASSWORD=
SQL_HOST=localhost
SQL_PORT=5432
```

