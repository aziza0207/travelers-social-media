## Локальный запуск приложения через docker-compose

Наберите команду в терминале

```shell
 docker compose up --build

```
Создайте файл .env в корневой директории

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
при необходимости найти разрешение на исполнение в терминале

```shell
chmod +x /entrypoint.sh
```

### После разворота

Swagger - http://0.0.0.0/api/docs/

Admin - http://0.0.0.0/admin/

## Локальный запуск приложения без докер

Создайте файл .env
```shell
SECRET_KEY=my_secret
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=Ваша база данных
SQL_USER=Ваше имя пользователя
SQL_PASSWORD=Ваш пароль
SQL_HOST=localhost
SQL_PORT=5432
```
Установите зависимости

```shell
pip install -r requirements.txt
```
Далее наберите команду
```shell
python manage.py migrate
```
для заполнения базы странами
```shell
python manage.py fetch_countries
```
для запуска приложения
```shell
python manage.py runserver
```

### После разворота

Swagger - http://0.0.0.0:8000/api/docs/

Admin - http://0.0.0.0::8000/admin/






