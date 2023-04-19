## Описание
REST API интерфейс для работы с сущностью оборудование
Реализованы:
get, post, put, delete методы
regex валидация в сериалайзере и модели

---
## Установка локально.

---


#### 1. Клонирование репозитория
```
md equipment
cd equipment
https://github.com/daminovvv/equipment.git
```

#### 2. Создание виртуального окружения
Создаём виртуальное окружение и активируем его
```
cd equipment
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

#### 4. Создание базы 
https://selectel.ru/blog/tutorials/how-to-create-databases-in-mysql/


#### 5. Настройка переменных окружения
1 - Создать файл `.env` в корне проекта

2 - Записать в этот файл следующее
```
MYSQL_DB=имя_БД
MYSQL_USER=пользователь_БД
MYSQL_PASSWORD=пароль_от_БД
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
```



#### 6. Создание миграций
1 - Активировать виртуальное окружение

на Windows
```
.\.venv\Scripts\activate
```

на Linux
```
source .venv/bin/activate
```

2 - выполнить миграции
```
python manage.py migrate
```


#### 7. Запуск сервера
Выполнить команду:

```
python manage.py runserver
```


Готово! =)

---