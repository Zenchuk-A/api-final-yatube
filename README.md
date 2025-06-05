# api-final-yatube
## Как запустить проект:

<ins>Клонировать репозиторий:</ins>

```
git clone https://github.com/Zenchuk-A/api-final-yatube.git
```
<ins>Перейти в него в командной строке:</ins>
 
```
cd api-final-yatube
```

<ins>Cоздать и активировать виртуальное окружение:</ins>  
Команда для Windows:
```
python -m venv env
```
```
source venv/Scripts/activate
```
Команда для Linux и macOS:
```
python3 -m venv env
```
```
source env/bin/activate
```
<ins>Обновить пакетный менеджер:</ins>  
```
python3 -m pip install --upgrade pip
```
<ins>Установить зависимости из файла requirements.txt:</ins>
```
pip install -r requirements.txt
```
<ins>Выполнить миграции:</ins>
```
python3 manage.py migrate
```
<ins>Запустить проект:</ins>
```
python3 manage.py runserver
```
