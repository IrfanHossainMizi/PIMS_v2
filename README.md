# web_gis103



this is geoDjango based website in this sector
Installation using pip:

pip install django-adminlte3
Add to installed apps:

INSTALLED_APPS = [
     # General use templates & template tags (should appear first)
    'adminlte3',
     # Optional: Django admin theme (must be before django.contrib.admin)
    'adminlte3_theme',

    ...
]

Don't forget to collect static

python manage.py collectstatic 


https://medium.com/analytics-vidhya/how-to-use-adminlte-in-django-225359ce8c72
# From my end
need connect to postgres database.<br />
pip install -r requirements.txt <br />
python manage.py makemigrations<br />
python manage.py migrate<br />
python manage.py runserver<br />
