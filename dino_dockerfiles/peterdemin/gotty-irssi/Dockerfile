FROM ubuntu:14.04

RUN apt-get -qqy update \
 && apt-get -y install curl irssi \
 && apt-get clean

RUN curl -sSL https://github.com/yudai/gotty/releases/download/v0.0.12/gotty_linux_amd64.tar.gz \
    | tar -xzvC /usr/bin/

EXPOSE 8080
CMD gotty -a 0.0.0.0 -p 8080 -w irssi
