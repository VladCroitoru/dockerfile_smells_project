FROM ubuntu:14.04
MAINTAINER include <francisco.cabrita@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -yq && \
    apt-get install -yq software-properties-common python-software-properties && \
    add-apt-repository -y ppa:pritunl/ppa && \
    apt-get update -yq && \
    apt-get install -yq pritunl && \
    apt-get clean -y && \
    apt-get autoremove -y

ADD mongodb.conf /etc/mongodb.conf
ADD pritunl.conf /etc/pritunl.conf

ADD cmdline.sh /usr/local/bin/cmdline.sh

EXPOSE 1194
EXPOSE 9700

ENTRYPOINT ["/usr/local/bin/cmdline.sh"]

CMD ["/usr/bin/tail", "-f", "/var/log/pritunl.log"]
