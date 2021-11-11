FROM alpine:edge
MAINTAINER Derren Desouza <derrend@yahoo.co.uk>

COPY decodescript.py /

RUN echo 'http://dl-cdn.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories && \
    apk add --no-cache py-m2crypto

ENTRYPOINT ["python","decodescript.py"]
