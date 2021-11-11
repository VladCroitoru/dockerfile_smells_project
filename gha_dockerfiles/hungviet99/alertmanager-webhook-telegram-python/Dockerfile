FROM alpine:3.7

LABEL maintainer "Carlos Augusto Malucelli <malucellicarlos@gmail.com>"

RUN apk update \
                && apk add py3-pip bash gcc python3-dev musl-dev git libffi-dev openssl-dev \
                && rm -rf /var/cache/apk/* \
                && git clone https://github.com/hungviet99/alertmanager-webhook-telegram-python.git \
                && pip3 install -r alertmanager-webhook-telegram-python/requirements.txt

WORKDIR /alertmanager-webhook-telegram-python

RUN chmod +x /alertmanager-webhook-telegram-python/run.sh

RUN chmod +x /alertmanager-webhook-telegram-python/flaskAlert.py

EXPOSE 9119

ENTRYPOINT ["./run.sh"]