
python2 manage.py createsuperuser

new console)python2 manage.py runserver 0.0.0.0:8000
new console)cd xls-messager/proj
celery -A proj worker --loglevel=DEBUG
new console)redis-server

web)visit 127.0.0.1:8000/admin
set your stmp server
visit /asyncmailer, use it
