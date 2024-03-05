***
_Репозиторий на Github [ссылка](https://github.com/JuliaBars/fastapi_django_integration_encost)._

**ООО «ЭНКОСТ»** - услуги для промышленных предприятий по всей России. [сайт](https://encost.com/)

#### Интеграция FastAPI в Django проект (тестовое задание)

---
OpenAPI документация `http://127.0.0.1:8000/docs`

Django админка: `http://127.0.0.1:8000/django/admin`

Для использования админки необходимо из директории с manage.py выполнить команду 
```python
python manage.py createsuperuser
```
### Endpoints:

`api/v1/endpoints_states` - get с limit offset для просмотра объектов EndpointStates
`api/v1/endpoint_states` - возвращает ответ на задание 3.d из ТЗ
`api/v1/endpoint_states_async` - асинк версия возвращает ответ на задание 3.d из ТЗ

---
Сборка проекта:
```python
python -m venv venv
. venv/Scripts/activate - Windows
. venv/bin/activate - Linux
pip install -r requirements.txt
cd encost/
```

Для запуска проекта на WSGI 
```python
uvicorn encost.wsgi:app --reload
```
Для запуска на ASGI

```python
uvicorn encost.asgi:app --reload
```

:point_right: Мой телеграм @JuliaBarss
