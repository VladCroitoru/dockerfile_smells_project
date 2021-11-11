FROM python:3.5.2

MAINTAINER fabiobatalha@gmail.com

COPY . /app

WORKDIR /app

RUN python setup.py install
RUN python setup.py nosetests --with-coverage

CMD ["playchess", "--help"]