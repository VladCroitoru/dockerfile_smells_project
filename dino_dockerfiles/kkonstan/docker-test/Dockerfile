FROM ubuntu:latest

RUN apt-get -y update
RUN apt-get -y install socat

CMD socat PIPE tcp-listen:${PORT:-7},fork

EXPOSE 7
