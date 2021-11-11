FROM ubuntu:16.04
MAINTAINER Eric Adamski "eric.adamski@mb3online.com"

ENV DEBIAN_FRONTEND noninteractive

# Install packages
ADD provision.sh /provision.sh
ADD serve.sh /serve.sh

ADD supervisor.conf /etc/supervisor/conf.d/supervisor.conf

RUN chmod +x /*.sh

RUN ./provision.sh

EXPOSE 80 22 35729 9876
CMD ["/usr/bin/supervisord"]
