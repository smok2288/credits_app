# credits_app
Приступаем к работе. Клонируем репозиторий:
git clone <repository_url> cd <repository_name> 

Создайте образ Docker:
docker-compose build 

Запустите контейнеры Docker:
docker-compose up -d Флаг -d используется для запуска контейнеров в фоновом режиме.

Инициализируйте проект и базу данных Django: 
docker-compose exec web python manage.py migrate

Доступ к серверу разработки Django: 
откройте веб-браузер и перейдите по адресу http://localhost:8000/.

Теперь вы можете получить доступ к своему приложению Django, работающему в контейнерах Docker.

Остановка приложения Чтобы остановить приложение и завершить работу контейнеров Docker, выполните:
docker-compose down
