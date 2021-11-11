FROM ubuntu:xenial

RUN apt update
RUN apt install -y xnbd-server

COPY entrypoint.sh /entrypoint.sh

EXPOSE 8520

ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
