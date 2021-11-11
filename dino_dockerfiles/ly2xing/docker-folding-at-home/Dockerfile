# This is a Dockerfile to create a FAH Client on Ubuntu 12.04
#
# VERSION 0.0

# use Ubuntu 12.04 image provided by docker.io
FROM ubuntu:12.04

MAINTAINER Olivier Dossmann, olivier+dockerfile@dossmann.net

# Get noninteractive frontend for Debian to avoid some problems:
#    debconf: unable to initialize frontend: Dialog
ENV DEBIAN_FRONTEND noninteractive

# Install wget
RUN apt-get install -y wget bzip2

# Download and install FAHClient
RUN wget -O fahclient_7.4.4_amd64.deb "https://fah.stanford.edu/file-releases/public/release/fahclient/debian-testing-64bit/v7.4/fahclient_7.4.4_amd64.deb" --no-check-certificate \
  && dpkg -i fahclient_7.4.4_amd64.deb

# Add configuration file to use
ADD config.xml /etc/fahclient/

RUN sed -i "s/'%USER%'/'"$USER"'/" /etc/fahclient/config.xml
RUN sed -i "s/'%TEAM%'/'"$TEAM"'/" /etc/fahclient/config.xml
RUN sed -i "s/'%POWER%'/'"$POWER"'/" /etc/fahclient/config.xml
RUN sed -i "s/'%PASSKEY%'/'"$PASSKEY"'/" /etc/fahclient/config.xml

RUN chown fahclient:root /etc/fahclient/config.xml

# Open some ports: 7396(Folding web client)
EXPOSE 7396

# Launch FAHClient
CMD /etc/init.d/FAHClient start && tail -F /var/lib/fahclient/log.txt
#CMD ["/etc/init.d/FAHClient", "start", "&&", 'tail', '-F', '/var/lib/fahclient/log.txt']
