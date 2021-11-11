FROM ubuntu:14.04

COPY ./certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt

ADD https://github.com/nickschuch/marco-docker/releases/download/0.0.1/marco-docker-Linux-x86_64 /marco-docker
RUN chmod a+x /marco-docker

CMD ["/marco-docker"]
