FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code
ADD requirements.txt /code/

RUN apt-get -y update && apt-get install -y libzbar-dev
RUN pip install -r requirements.txt

ADD . /code/

EXPOSE 8000
ENTRYPOINT []
CMD ['python', 'manage.py', 'runserver', '0.0.0.0:8000']
