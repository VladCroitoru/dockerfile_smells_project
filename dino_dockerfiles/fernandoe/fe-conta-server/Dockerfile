FROM fernandoe/docker-python:3.7.0-alpine3.8

ADD ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

ADD ./docker/run.sh /run.sh
ADD ./src /app

WORKDIR /app

CMD ["/run.sh"]
