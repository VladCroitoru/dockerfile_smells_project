FROM ubuntu:14.04

COPY ./certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt

ADD https://github.com/nickschuch/marco-ecs/releases/download/0.0.2/marco-ecs-Linux-x86_64 /marco-ecs
RUN chmod a+x /marco-ecs

CMD ["/marco-ecs"]
