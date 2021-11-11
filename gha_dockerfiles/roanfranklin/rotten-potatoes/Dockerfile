FROM python:3.8

MAINTAINER roanfranklin@gmail.com

WORKDIR /code

COPY ./src/requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

COPY ./src .

EXPOSE 5000

CMD [ "gunicorn", "--workers=3", "--bind", "0.0.0.0:5000", "app:app" ]