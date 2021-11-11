FROM python:3.5
ENV PYTHONUNBUFFERED 1

RUN echo America/New_York > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata

RUN apt-get update -qq && apt-get install -y git-core libmemcached-dev
RUN pip install -U pip
RUN pip install honcho
RUN mkdir /app
WORKDIR /app

ADD requirements.txt /app/
RUN pip install -r requirements.txt

EXPOSE 8000

ADD . /app/

CMD honcho start web
