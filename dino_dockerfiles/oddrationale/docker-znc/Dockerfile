# Docker image running ZNC 1.6
#
# VERSION   0.2.0

FROM ubuntu:16.04
MAINTAINER Dariel Dato-on <oddrationale@gmail.com>

# Compile ZNC from source
ADD http://znc.in/releases/znc-1.6.3.tar.gz /tmp/
ADD build.sh /tmp/
RUN /tmp/build.sh

# Create a 'znc' user so we don't run znc as root. HOME=/var/znc
RUN adduser --system --group --home /var/znc --shell /bin/bash znc
USER znc
ENV HOME /var/znc

# Add data volume to hold ZNC config files
VOLUME ["/var/znc"]

ENTRYPOINT ["/usr/local/bin/znc"]
CMD ["--foreground"]
