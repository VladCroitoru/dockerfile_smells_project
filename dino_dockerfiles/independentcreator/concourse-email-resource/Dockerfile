FROM python:3-alpine
RUN apk add --update postfix build-base libxml2-dev libxslt-dev python3-dev \
&&  pip install jinja2 html2text inlinestyler \
&&  rm -rf /var/cache/* /root/.cache \
&&  apk del build-base python3-dev
COPY opt /opt
