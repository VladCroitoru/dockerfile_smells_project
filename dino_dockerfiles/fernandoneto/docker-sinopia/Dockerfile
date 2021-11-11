FROM cusspvz/node:4.1.2
MAINTAINER Fernando Neto <fernado.neto@junglecloud.com>

RUN mkdir -p /sinopia;

ADD . /sinopia
WORKDIR /sinopia

RUN apk add --update make g++ nfs-utils python; \
    npm install -g sinopia sinopia-ldap js-yaml; \
    apk del make g++ python;

EXPOSE 4873

VOLUME ["/data"]

ENTRYPOINT /sinopia/bin/entrypoint.sh
