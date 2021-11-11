FROM alpine

MAINTAINER Weiyan Shao <lighteningman@gmail.com>

RUN apk --update add nginx openssh curl rsync && \
    adduser rsync -D && \
    passwd rsync -d password_that_should_never_be_used

COPY ./fs-overlay/ /

ADD https://github.com/just-containers/s6-overlay/releases/download/v1.16.0.1/s6-overlay-amd64.tar.gz /tmp/s6-overlay.tar.gz
RUN tar xvfz /tmp/s6-overlay.tar.gz -C / && rm /tmp/s6-overlay.tar.gz

EXPOSE 22 80
VOLUME /rsync
VOLUME /etc/ssh/keys/

ENTRYPOINT [ "/init" ]
