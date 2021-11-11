FROM ubuntu:14.04

COPY ./certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt

ADD https://github.com/nickschuch/marco-compose/releases/download/0.0.1/marco-compose-Linux-x86_64 /marco-compose
RUN chmod a+x /marco-compose

CMD ["/marco-compose"]
