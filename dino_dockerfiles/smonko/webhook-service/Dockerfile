FROM debian:stable-slim
MAINTAINER Stefan Monko, PosAm s.r.o.

RUN apt-get -y update && \
    apt-get -y install webhook && \
    apt-get -y install git && \
    apt-get -y install openssh-client && \
    printf '\n' | ssh-keygen -N '' && \
    git config --global http.sslVerify false

CMD ["/usr/bin/webhook", "-verbose", "-hooks=/etc/webhook/hooks.json", "-hotreload"]
