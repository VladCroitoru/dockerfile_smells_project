FROM python:2.7.12

# RUN apk update && apk add py-virtualenv mariadb-dev
RUN apt-get update && apt-get install -y --force-yes python-virtualenv libmysqlclient-dev
RUN virtualenv -p python2.7 --no-site-packages /virtualenv

ADD requirements.txt /app/requirements.txt
RUN /virtualenv/bin/pip install -r /app/requirements.txt

ADD . /app

EXPOSE 8878
WORKDIR /app

CMD /virtualenv/bin/python /app/manage.py runserver 0.0.0.0:8878
