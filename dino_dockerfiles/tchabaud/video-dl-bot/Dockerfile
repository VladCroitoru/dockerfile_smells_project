FROM python:alpine

COPY requirements.txt /opt/
COPY entrypoint.sh /opt/

RUN addgroup -g 5000 dckrusers && adduser -S -s /sbin/nologin -u 5000 -G dckrusers docker

RUN apk --update add --virtual build-deps python3-dev gcc musl-dev libressl-dev libffi-dev \
    && apk --update add ffmpeg python3 libffi libressl \
    && pip3 install --upgrade pip \
    && pip3 install -U -r /opt/requirements.txt \
    && apk del build-deps

COPY ./main.py /opt/main.py
COPY ./proxy.py /opt/proxy.py

RUN chmod a+x /opt/*.py /opt/*.sh

USER docker
ENTRYPOINT [ "/opt/entrypoint.sh" ]
