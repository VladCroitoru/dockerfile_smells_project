FROM golang:alpine
MAINTAINER Erik Redding <erik@erikerikerik.com>

# install base services and stuff we need
RUN set -x \
    && echo "@edge http://nl.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories \
    && echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories \
    && echo "@community http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
    && apk --update upgrade \
    && apk add --no-cache runit@community=2.1.2-r3 git python3 bash bash-completion vim make netcat-openbsd \
    && apk add --no-cache --virtual=build-dependencies wget ca-certificates  \
    && wget -q "https://bootstrap.pypa.io/get-pip.py" -O /dev/stdout | python3  \
    && apk del build-dependencies  \
    && rm -rf /var/cache/apk/*  \
    && mkdir -p /etc/service  \
    \
    && adduser -u 1000 -g 1000 -D user \
    \
    && install -o user -g user -d /app \
    && install -o user -g user -d /app/logs \
    && go get \
            github.com/pierrre/gotestcover \
            github.com/tsg/goautotest \
            github.com/motemen/gore \
            github.com/Masterminds/glide


ENV GO15VENDOREXPERIMENT=1

ADD https://raw.githubusercontent.com/docker-library/golang/master/1.7/go-wrapper /usr/local/bin/go-wrapper
RUN chmod +x /usr/local/bin/go-wrapper \
    && mkdir -p /etc/pki/tls/certs

CMD ["/bin/bash"]
