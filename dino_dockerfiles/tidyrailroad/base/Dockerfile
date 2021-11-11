FROM alpine:3.4
MAINTAINER Emory Merryman emory.merryman@gmail.com
RUN \
    apk update && \
    apk upgrade && \
    apk add docker && \
    apk add sudo && \
    adduser -D user && \
    true
VOLUME ["/etc/sudoers.d"]
VOLUME ["/usr/local/sbin"]

