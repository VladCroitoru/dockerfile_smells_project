FROM    pblittle/docker-logstash
MAINTAINER Josh Cox <josh 'at' webhosting coop>

# Environment variables
ENV ICINGASH_UPDATED 20160806
ENV DEBIAN_FRONTEND noninteractive

# Add debmon repository key to APT.
#RUN wget -O - http://debmon.org/debmon/repo.key 2>/dev/null | apt-key add -
# Add Debian Backports and Debmon repositories and update package lists again.
#RUN echo "deb http://http.debian.net/debian wheezy-backports main" >> /etc/apt/sources.list
#RUN echo "deb http://debmon.org/debmon debmon-wheezy main" >> /etc/apt/sources.list
#RUN add-apt-repository ppa:formorer/icinga
RUN apt-get -qq update
# Install icinga2 and nsca so we can send log events upstream
RUN apt-get -y install icinga2
RUN apt-get -y install --no-install-recommends nagios-plugins nsca
# Clean up some.
RUN apt-get clean
# To install feature add lines like these in your final Dockerfile
# Enable IDO for MySQL. This is needed by icinga-web.
# RUN icinga2 enable feature ido-mysql

ADD ./start.sh /start.sh
RUN chmod 755 /start.sh
ENTRYPOINT ["/start.sh"]
