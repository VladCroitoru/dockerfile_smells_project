FROM quay.io/letsencrypt/letsencrypt
MAINTAINER Martin Venuš <martin.venus@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
ENV TERM xterm

RUN apt-get update && apt-get -y install docker.io

ADD start.sh /bin/start.sh

ENTRYPOINT [ "/bin/start.sh" ]
