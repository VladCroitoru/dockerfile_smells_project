FROM python:3-alpine
RUN apk add --update postfix build-base libxml2 libxml2-dev libxslt libxslt-dev python3-dev \
&&  pip install jinja2 html2text inlinestyler \
&&  rm -rf /var/cache/* /root/.cache \
&&  apk del build-base python3-dev libxslt-dev libxml2-dev
MAINTAINER mail@martindomke.net
COPY opt /opt
