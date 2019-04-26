# Flask API. Тестовое задание.
---


Задание: Создать API RESTfull для приложения на Flask.

За основу взят микроблог коротких текствых сообщений на Flask. База данных sqlite3.  

Инстукция по установке:
- cоздаем виртуальное окружение, например:  
    python3 -m venv myvenv  
- активируем виртуальную среду:  
    source myvenv/bin/activate  
- далее установливаем зависимости из requirements.txt:  
    pip3 install -r requirements.txt  
- перед запуском приложения устанавливаем переменную среды введя следующую команду в консоли:  
    export FLASK_APP=microblog.py
- комманды для базы данных:  
    flask db init  
    flask db migrate  
    flask db upgrade    
- запускаем приложение командой:  
    flask run  

После успешного запуска нужно зайти с помощью браузера по адрессу http://127.0.0.1:5000 и зарегистрировать несколько пользователей, так как данное API не реализует функционала для работы с пользователями. Так же можно создать сообщения для микроблога, используя веб браузер.  

## API реализует следующий функционал:

* /api/posts/ - GET метод отобразит список всех постов блога.
* /api/posts/ - POST метод создаст новый пост если пользователь зарегистрирован.
* /api/posts/id/ - GET - отобразит детальную информацию о посте с конкретным id.
* /api/posts/id/ - PUT - автор поста имеет возможность его редактировать.
* /api/posts/id/ - DELETE - автор поста имеет возможность его удалить.

## Примеры работы с API (с помощью консольной программы http)

* Вывести список всех сообщений микроблога:  
    http GET localhost:5000/api/posts

* Вывести одно сообщеие с соответсвующим id:  
    http GET localhost:5000/api/posts/3

* Для создания, редактирования и удаления поста необходимо получить токен. Например (пользователь - susan с паролем - cat):  
    http --auth susan:cat POST localhost:5000/api/tokens

* Создать пост используя полученный токен:  
    http POST localhost:5000/api/posts body="Created post" \  
"Authorization:Bearer zPCX+xqvpa0o5qP34+3hqQeSS9UfCIDg"  

* Обновить пост:  
    http PUT localhost:5000/api/posts/14 body="Updated post" \  
"Authorization:Bearer zPCX+xqvpa0o5qP34+3hqQeSS9UfCIDg"  

* Удалить пост:  
    http DELETE localhost:5000/api/posts/15 "Authorization:Bearer zPCX+xqvpa0o5qP34+3hqQeSS9UfCIDg"  

* Удалить токен (применяется в целях безопасности):  
    http DELETE localhost:5000/api/tokens "Authorization:Bearer Ijthgqh3cRa9361fK1H6D6qlQxhpK+/9"

