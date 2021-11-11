FROM mytardis/filters-essentials AS base

ENV LOG_LEVEL info
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

FROM base AS builder

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -U pip setuptools numpy
RUN pip3 install -r requirements.txt

ADD . /app

CMD ["celery", "--app=tardis.celery.app", "worker", "--queues=filters", "--loglevel=${LOG_LEVEL}"]

FROM builder AS test

RUN pip3 install -r requirements-test.txt

RUN mkdir /var/store

# This will keep container running...
CMD ["tail", "-f", "/dev/null"]
