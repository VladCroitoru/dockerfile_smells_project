FROM python:2.7
MAINTAINER Alan Craig <acraig94@gmail.com>

RUN apt-get -qqy update
RUN apt-get -qqy install git libcurl4-openssl-dev curl build-essential python

RUN mkdir -p /opt/flask_app
WORKDIR /opt/flask_app

ADD requirements.txt /opt/flask_app

RUN pip install -r requirements.txt

RUN uwsgi --build-plugin https://github.com/unbit/uwsgi-consul

ADD uwsgi-consul.ini /opt/flask_app/
ADD app.py /opt/flask_app/ 

ENTRYPOINT [ "uwsgi", "--ini", "uwsgi-consul.ini", "--ini", "uwsgi-consul.ini:server1" ]
CMD []