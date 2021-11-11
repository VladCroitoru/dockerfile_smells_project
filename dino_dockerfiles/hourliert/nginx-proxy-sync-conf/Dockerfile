FROM bashell/alpine-bash

MAINTAINER Thomas Hourlier <thomas.hourlier@cnode.fr>

VOLUME /htpasswd
VOLUME /vhost.d

WORKDIR /config

COPY src/entrypoint.sh .

ENTRYPOINT /config/entrypoint.sh
