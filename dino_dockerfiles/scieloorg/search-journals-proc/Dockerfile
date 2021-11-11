FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

MAINTAINER tecnologia@scielo.org

RUN apk --update add --no-cache \
    git gcc build-base zlib-dev jpeg-dev curl libxml2-dev libxslt-dev py3-lxml libressl libressl-dev ca-certificates

COPY . /app

RUN pip install --upgrade pip
RUN chmod -R 755 /app/*

WORKDIR /app

RUN python setup.py install

RUN chown -R nobody:nogroup /app
USER nobody

CMD ["update_search", "--help"]

