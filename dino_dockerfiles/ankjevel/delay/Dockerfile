FROM alpine:3.5

ENV WEB_CONCURRENCY=4
ENV DEBUG=False

RUN apk add --update python python-dev py-pip build-base ca-certificates libffi-dev

WORKDIR  /app

COPY ./setup.py /app/setup.py

RUN pip install --upgrade pip && pip install gunicorn && pip install /app

COPY ./delay /app/delay

EXPOSE 80

CMD gunicorn -b 0.0.0.0:80 --timeout 3600 --graceful-timeout 3600 delay:app
