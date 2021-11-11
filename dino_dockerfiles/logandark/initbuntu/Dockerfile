FROM library/ubuntu:16.04
LABEL maintainer "logandarklock@gmail.com"

ENV container docker
STOPSIGNAL SIGRTMIN+3

RUN apt-get update && apt-get install dbus -y --force-yes

COPY initbuntu.sh /sbin/initbuntu.sh
RUN chmod 0744 /sbin/initbuntu.sh

CMD /sbin/initbuntu.sh
