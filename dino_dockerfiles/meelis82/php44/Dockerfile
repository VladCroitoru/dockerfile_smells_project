FROM dockerizedrupal/base-debian-wheezy:1.1.0

MAINTAINER Meelis Valgeväli <meelis82@gmail.com>

LABEL vendor=dockerizedrupal.com

ENV TERM xterm

ADD ./src /src

RUN /src/entrypoint.sh build

EXPOSE 8002

ENTRYPOINT ["/src/entrypoint.sh", "run"]
