#
# Caddy web server for hkjn.me.
#
# TODO: Set up x86_64 vs armv7l base images to build on separate tags? Or separate repo?
FROM resnullius/alpine-armv7l

MAINTAINER Henrik Jonsson <me@hkjn.me>

ENV USER web
ENV HOME /home/$USER
ENV GOPATH $HOME
ENV PATH /usr/bin:/usr/sbin:/sbin:$GOPATH/bin

RUN apk --no-cache add bash vim git go && \
    adduser -D $USER -s /bin/bash && \
    go get github.com/mholt/caddy

COPY Caddyfile $GOPATH/src/hkjn.me/caddyweb/

WORKDIR $GOPATH/src/hkjn.me/caddyweb

USER $USER

ENTRYPOINT ["caddy"]
