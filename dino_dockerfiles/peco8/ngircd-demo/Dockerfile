# Using official ubuntu base image
FROM ubuntu:trusty

MAINTAINER "Toshiki Inami <t-inami@arukas.io>"

# ENV DEBIAN_FRONTEND noninteractive

# Install ngircd and supervisor
RUN apt-get update -q && \
    apt-get install -y -qq \
                      ngircd \
                      supervisor && \
    apt-get clean && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Congigure ngircd
COPY ngircd/ngircd.conf /etc/ngircd/ngircd.conf
COPY ngircd/ngircd.motd /etc/ngircd/ngircd.motd

# Configure supervisord
COPY locale /etc/default/locale
COPY supervisor.conf /etc/supervisor/conf.d/ngircd.conf

# Listening on TCP port 6697
EXPOSE 6667

CMD ["/usr/bin/supervisord"]
