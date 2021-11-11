FROM python:2.7.9-slim
MAINTAINER espen@mrfjo.org
ENV LC_ALL C
ENV DEBIAN_FRONTEND noninteractive

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apt-get update && \
    apt-get install -y  --no-install-recommends --force-yes git
COPY docker-requirements.txt /usr/src/app/
RUN pip install git+https://github.com/django-nonrel/django@nonrel-1.6
RUN pip install git+https://github.com/django-nonrel/mongodb-engine.git
RUN pip install pymongo==2.8 docker-py simplejson

COPY . /usr/src/app

EXPOSE 8080
ENTRYPOINT ["./entrypoint.sh"]

