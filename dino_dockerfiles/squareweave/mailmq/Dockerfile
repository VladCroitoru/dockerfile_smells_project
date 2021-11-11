FROM python:3.5

RUN set -xe && \
    mkdir /app && \
    true

WORKDIR /app
CMD celery -A mailmq.server worker --uid=1 --loglevel=INFO

COPY requirements.txt /app/

RUN set -xe && \
    pip install -r requirements.txt && \
    true

COPY . /app/
