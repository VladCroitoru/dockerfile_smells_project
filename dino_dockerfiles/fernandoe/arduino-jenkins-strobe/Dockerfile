FROM fernandoe/docker-python:0.0.1
MAINTAINER Fernando Espíndola <fer.esp@gmail.com>

RUN apt-get install -y supervisor

ENV C_FORCE_ROOT foo

RUN mkdir -p /app
WORKDIR /app

VOLUME /db

RUN mkdir -p /opt/arduino
ADD ./sandbox/requirements.txt /opt/arduino/
ADD ./sandbox/gunicorn_config.py /opt/arduino/
ADD ./sandbox/startup_web.sh /opt/arduino/
ADD ./sandbox/startup_celery.sh /opt/arduino/
RUN pip install -r /opt/arduino/requirements.txt
COPY ./arduino /app

EXPOSE 8000

ADD ./sandbox/supervisord.conf /etc/supervisor/conf.d/
run ln -s /home/docker/code/supervisor-app.conf

CMD ["supervisord", "-n"]
