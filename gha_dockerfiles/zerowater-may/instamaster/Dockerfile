FROM python:3.9.0

RUN echo "104"

WORKDIR /home/

RUN git clone https://github.com/zerowater-may/instamaster.git

RUN ls

RUN mv instamaster django_pinterest

RUN ls

WORKDIR /home/django_pinterest/

RUN ls

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

# RUN pip install environ
# RUN echo "SECRET_KEY=5nb@rlfrak967e6#g4pr)8&s2tf*zsquyhbh7_x52d@7g+__+@" > .env
# 퇴근해야되서 변경 안댐 

EXPOSE 8000

# RUN python -c "import django; django.setup(); \
#    from django.contrib.auth.management.commands.createsuperuser import get_user_model; \
#    get_user_model()._default_manager.db_manager('zerowater').create_superuser( \
#    username='zerowater', \
#    email='kys9805331@naver.com', \
#    password='fkaustkfl123!')"

CMD ["bash","-c","python manage.py collectstatic --noinput --settings=pragmatic.settings.deploy && python manage.py migrate --settings=pragmatic.settings.deploy && gunicorn pragmatic.wsgi --env DJANGO_SETTINGS_MODULE=pragmatic.settings.deploy --bind 0.0.0.0:8000"]
# python manage.py migrate --fake --settings=pragmatic.settings.deploy && python manage.py migrate --fake naverapp zero --settings=pragmatic.settings.deploy && python manage.py migrate --fake emailapp zero --settings=pragmatic.settings.deploy && python manage.py migrate --fake emailapp zero --settings=pragmatic.settings.deploy