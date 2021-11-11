FROM alpine:edge
MAINTAINER admin@tropicloud.net

RUN adduser -h /app -s /bin/sh -D chaordic chaordic && \
    echo "chaordic ALL = NOPASSWD : ALL" >> /etc/sudoers && \
    apk --update add git nodejs nginx sudo s6

ADD . /app
WORKDIR /app
USER chaordic
RUN sudo npm install && \
    sudo chown -R chaordic:chaordic .

EXPOSE 8080
CMD s6-svscan service
