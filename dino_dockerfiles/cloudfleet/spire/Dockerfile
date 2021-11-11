FROM alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

RUN apk add py3-psycopg2

ADD requirements.txt /code/

RUN pip3 install -r requirements.txt

ADD . /code/

CMD python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000
