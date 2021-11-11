FROM dockerfile/ubuntu

MAINTAINER Panagiotis Moustafellos <pmoust@gmail.com>

RUN apt-get update && apt-get install -y dnsmasq dnsutils

ADD dnsmasq.conf /etc/dnsmasq.conf

ADD start.sh /start.sh
RUN chmod +x /start.sh

ENTRYPOINT ["/bin/bash", "/start.sh"]
EXPOSE 53
