FROM       alpine
MAINTAINER Mesosphere <team@mesosphere.com>
EXPOSE     443

RUN echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing" \
     >> /etc/apk/repositories \
    && apk -U add openssl tengine@testing

ADD config /config
ENTRYPOINT [ "/config/run" ]
