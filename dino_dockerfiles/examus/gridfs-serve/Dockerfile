FROM python:2.7

WORKDIR app
ADD requirements.txt requirements.txt
RUN pip install uwsgi
RUN pip install -r requirements.txt
COPY . .
CMD uwsgi --socket=:8001 --module=wsgi:app
