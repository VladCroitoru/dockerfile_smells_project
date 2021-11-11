FROM alpine:3.13

MAINTAINER "Mateo Boudet <mateo.boudet@inrae.fr>"

COPY requirements.txt /tmp/requirements.txt

RUN apk add --no-cache \
    python3 \
    bash \
    nano \
    nginx \
    uwsgi \
    uwsgi-python3 \
    supervisor \
    ca-certificates \
    postgresql-libs \
    at \
    nodejs nodejs-npm \
    gcc g++ libstdc++ make \
    wget curl unzip && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    apk add --no-cache --virtual .build-deps gcc musl-dev python3-dev postgresql-dev && \
    pip3 install -r /tmp/requirements.txt && \
    apk --purge del .build-deps && \
    rm /etc/nginx/conf.d/default.conf && \
    rm -r /root/.cache

COPY docker/nginx.conf /etc/nginx/
COPY docker/nginx_askosite.conf /etc/nginx/conf.d/
COPY docker/uwsgi.ini /etc/uwsgi/
COPY docker/supervisord.conf /etc/supervisord.conf

COPY . /askosite

WORKDIR /askosite

RUN mkdir /var/log/askosite
RUN chown nginx:nginx /var/log/askosite

RUN npm install --silent
RUN npm run --silent prod

COPY start_askosite.sh /start_askosite.sh

ENTRYPOINT "/start_askosite.sh"
