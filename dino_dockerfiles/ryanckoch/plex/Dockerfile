FROM ubuntu:14.04

VOLUME /config

ENV DEBIAN_FRONTEND noninteractive

ENV HOME /root

ADD plexmediaserver /default_plexmediaserver
ADD firstrun.sh /etc/my_init.d/firstrun.sh

RUN apt-get update && \
    apt-get install -y wget curl && \
    ln -s -f /bin/true /usr/bin/chfn && \
	chmod +x /etc/my_init.d/firstrun.sh

EXPOSE 32400

CMD ["/etc/my_init.d/firstrun.sh"]
