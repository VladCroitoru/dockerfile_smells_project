FROM python:2.7.13-alpine
MAINTAINER Genadi Postrilko <genadipost@gmail.com>

RUN addgroup -g 433 runner \
    && adduser -u 431 -G runner -h /home/runner -D -s /sbin/nologin runner \
    && apk add --update git \
    && pip install virtualenv

USER runner

WORKDIR /home/runner

RUN     git clone https://github.com/sensu/sensu-mkdocs \ 
        && cd sensu-mkdocs \
        && virtualenv venv \
        && . venv/bin/activate \
        && pip install -r requirements.txt

EXPOSE 8080

CMD cd sensu-mkdocs && . venv/bin/activate && mkdocs serve --dev-addr=0.0.0.0:8080
