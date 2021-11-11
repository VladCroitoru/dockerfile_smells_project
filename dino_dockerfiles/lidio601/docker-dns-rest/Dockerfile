FROM alpine:latest
MAINTAINER "Fabio Cigliano"

WORKDIR /app

ENV PY=2.7.15-r1
COPY ./requirements.txt requirements.txt
RUN apk add --update python=${PY} python-dev=${PY} \
                     gcc libgcc libc-dev py2-pip libev \
    && pip install -r requirements.txt \
    && apk del python-dev gcc libgcc libc-dev py2-pip libev \
    && rm -rf /tmp/* \
    && rm -rf /var/cache/apk/*

EXPOSE 80
COPY . .

ENTRYPOINT ["./docker_dnsrest"]
