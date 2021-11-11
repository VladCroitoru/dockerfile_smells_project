FROM ubuntu:18.10

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:certbot/certbot && \
    apt-get update && \
    apt-get install -y certbot

WORKDIR /etc/letsencrypt
VOLUME /etc/letsencrypt

ENTRYPOINT ["certbot"]
