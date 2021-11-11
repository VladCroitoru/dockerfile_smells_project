FROM sdurrheimer/alpine-glibc

MAINTAINER Roman Mohr <rmohr@redhat.com>

ENV VERSION v0.0.1 

ENV NAME ovirt-prometheus-bridge-$VERSION

ENV SOURCE_URL https://github.com/rmohr/ovirt-prometheus-bridge/releases/download/$VERSION/$NAME.tar.gz

RUN apk add --update curl && cd / && curl -L -O $SOURCE_URL && gunzip $NAME.tar.gz && tar xf $NAME.tar && mv $NAME/bin/ovirt-prometheus-bridge / && rm -rf $NAME.tar.gz $NAME && apk del curl && rm -rf /var/cache/apk/*

ENTRYPOINT ["/ovirt-prometheus-bridge"]
