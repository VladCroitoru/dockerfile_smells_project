FROM docker
MAINTAINER Tibor Sári <tiborsari@gmx.de>

ADD docker-dns /usr/local/bin

RUN apk update && apk add --no-cache bash

CMD ["/usr/local/bin/docker-dns"]