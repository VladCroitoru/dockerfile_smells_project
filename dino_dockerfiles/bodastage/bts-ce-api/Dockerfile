FROM ubuntu:16.04
LABEL maintainer Bodastage Engineering <engineering@bodastage.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y python python-pip python-virtualenv gunicorn netcat git wget zlib1g-dev libffi-dev \
    libssl-dev

# Setup flask application
RUN mkdir -p /deploy/
RUN mkdir -p /app
COPY ./requirements.txt /deploy/requirements.txt
RUN pip install -r /deploy/requirements.txt && pip install alembic virtualenv
WORKDIR /app

# Install python 3.7
RUN mkdir /tmp/Python37 \
    && cd /tmp/Python37 \
    && wget https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz \
    && tar xzf /tmp/Python37/Python-3.7.1.tgz \
    && cd /tmp/Python37/Python-3.7.1 \
    && ./configure \
    && make altinstall \
    && pip3.7 install -r /deploy/requirements.txt

# Create migrations and virtual env folder
RUN mkdir -p /migrations && chmod -R 777  /migrations && mkdir -p /python37 && chmod -R 777  /python37

RUN virtualenv -p /usr/local/bin/python3.7 /python37 \
    && chmod 777 /python37/bin/activate \
    && /python37/bin/activate \
    && pip3.7 install sqlalchemy alembic psycopg2-binary

COPY ./wait-for-it.sh /wait-for-it.sh
COPY ./migrate-and-start-web-server.sh /migrate-and-start-web-server.sh

RUN chmod 777 /wait-for-it.sh
RUN chmod 777 /migrate-and-start-web-server.sh 

EXPOSE 8181

# Start gunicorn
CMD ["/usr/bin/gunicorn", "--config", "/app/gunicorn_config.py", "wsgi:app"]
