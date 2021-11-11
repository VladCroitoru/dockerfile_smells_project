FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y libgdal-dev python-gdal npm netcat postgresql-client && ln -s /usr/bin/nodejs /usr/bin/node && npm install -g bower
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD docker-compose.yml /code/
ADD Dockerfile /code/
