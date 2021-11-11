# Dockerfile for building a SMTP/SPAM Sink in Docker

FROM debian:jessie
MAINTAINER  Emre Bastuz <info@emre>

# Environment 
ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8

# Get current & install packages
RUN apt-get update -y && \
	apt-get dist-upgrade -y && \
	apt-get install -y supervisor postfix

# Prepare supervisord
ADD dist/supervisord.conf /root/
RUN cp /root/supervisord.conf /etc/supervisor/

# Create directory for mails
RUN	mkdir -p /opt/spamsink/mails && chown -R nobody:nogroup /opt/spamsink

# Clean up
RUN	rm -rf /root/* && \
	apt-get autoremove -y && \
	apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Run smtp-sink
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/supervisord.conf"]
