FROM tvial/docker-mailserver:latest

MAINTAINER Thomas Hourlier <thomas.hourlier@cnode.fr>

WORKDIR /config

ADD src/entrypoint.sh .

VOLUME /tmp/docker-mailserver/

ENTRYPOINT /config/entrypoint.sh