
FROM python:3.6

WORKDIR /usr/src/

RUN git clone git://github.com/gpodder/mygpo.git

RUN apt-get install libpq-dev libjpeg-dev zlib1g-dev libwebp-dev libffi-dev

WORKDIR /usr/src/mygpo 

RUN pip install -r requirements.txt

EXPOSE 8000

RUN pip install gunicorn celery django-celery-beat

CMD [ "gunicorn", "-b", ":8000", "mygpo.wsgi" ]
