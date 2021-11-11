FROM python:2.7-alpine

RUN mkdir -p /app
WORKDIR /app

RUN apk --no-cache add \
    postgresql-dev

RUN apk --no-cache add \
    git \
    build-base \
    && git clone https://github.com/formspree/formspree.git . \
    && pip install -r requirements.txt \
    && pip install gunicorn gevent futures \
    && apk del build-base git

COPY run_server.sh ./run_server.sh

CMD ["./run_server.sh"]