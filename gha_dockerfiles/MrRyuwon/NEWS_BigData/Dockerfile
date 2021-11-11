FROM python:3.9.0

WORKDIR /home/

RUN echo "asadsadkf"

RUN git clone -b 8/11_3ban_class_commit_1 https://github.com/MrRyuwon/gis_3ban_1.git

WORKDIR /home/gis_3ban_1/

#RUN echo "SECRET_KEY=django-insecure-y*7(@vu)z_q$qmc5tee=dbuo$5f(!$rf@n)vsgfkipumfu(jp+" > .env

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=djangoProject2.settings.deploy && python manage.py migrate --settings=djangoProject2.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=djangoProject2.settings.deploy djangoProject2.wsgi --bind 0.0.0.0:8000"]