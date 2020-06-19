# ewords
Secret projects called "ewords"
1) Ставишь python на комп
2) Ставишь виртуальное окружение
python -m venv ewords_venv
ewords_venv\Scripts\activate.bat - активировать
ewords_venv\Scripts\deactivate.bat - деактивировать
2) Установка пакетов (requirements.txt я автоматом сгенерил):
pip install -r requirements.txt
3) Запускашь сервер (будет тут по дефолту - http://127.0.0.1:8000/):
python manage.py runserver