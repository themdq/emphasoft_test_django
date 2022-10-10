# Как запустить проект
Склонируйте репозиторий на локальную машину:
```bash
git clone https://github.com/themdq/emphasoft_test_django.git
```
Установите postgres

Установите виртуальное окружения
```bash
cd <path>/
```
```bash
python -m venv venv
```
Активируйте его(для unix систем) 
```bash
source venv/bin/activate
```

Установите зависимости
```bash
pip install -r requirements.txt
```
Зайдите в папку с manage.py 
```bash
cd <path>
```
Не забудьте вставить свои данные postgres в settings.py!
Проведите миграции
```bash
python manage.py makemigrations
python manage.py migrate
```
#### Создайте суперюзера
```bash
python manage.py createsuperuser
```
#### Запустите и радуйтесь
```bash
python manage.py runserver
```

