FROM tiangolo/uwsgi-nginx-flask:flask-python3.5
MAINTAINER Chris Jones "ipv6freely@gmail.com"

COPY requirements.txt /tmp/

RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

COPY ./app /app