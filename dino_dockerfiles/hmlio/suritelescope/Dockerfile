# suricata dockerfile by MO
#
# VERSION 16.03.5
FROM ubuntu:14.04.4
MAINTAINER MO

# Setup apt
RUN echo "deb http://ppa.launchpad.net/oisf/suricata-stable/ubuntu trusty main" >> /etc/apt/sources.list && \
    echo "deb-src http://ppa.launchpad.net/oisf/suricata-stable/ubuntu trusty main" >> /etc/apt/sources.list && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 9F6FC9DDB1324714B78062CBD7F87B2966EB736F && \
    apt-get update -y && \
    apt-get dist-upgrade -y
ENV DEBIAN_FRONTEND noninteractive

# Install packages
RUN apt-get install -y supervisor suricata wget make gcc libpcap-dev libjansson-dev git

# Setup user, groups and configs
RUN addgroup --gid 2000 tpot && \
    adduser --system --no-create-home --shell /bin/bash --uid 2000 --disabled-password --disabled-login --gid 2000 tpot
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD suricata.yaml /etc/suricata/suricata.yaml

# Download the latest EmergingThreats ruleset
#RUN wget --no-parent -l1 -r --no-directories -P /etc/suricata/rules/ https://rules.emergingthreats.net/open/suricata/rules/

# Clean up
RUN apt-get remove -y make gcc libpcap-dev libjansson-dev git && \
    apt-get autoremove -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Start suricata
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/supervisord.conf"]
