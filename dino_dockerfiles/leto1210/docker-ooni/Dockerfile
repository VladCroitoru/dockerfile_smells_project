FROM python:2.7.14
ENV PYTHONUNBUFFERED 1
MAINTAINER leto1210 version 1.3

# Setup the locales in the Dockerfile
RUN set -x \
    && apt-get update \
    && apt-get install locales -y \
    && locale-gen en_US.UTF-8

## Upgrade env and prerequisites ###
RUN apt-get install -yq python-pip python-dev libgeoip-dev libpcap-dev libdumbnet-dev \
                          build-essential libssl-dev libffi-dev libssl1.0.0 \
                          tor-geoipdb virtualenv torsocks tor
RUN rm -rf /var/lib/apt/lists/*

### Installation of ooniprobe ###
RUN pip install --upgrade pip
RUN pip install --upgrade ooniprobe

### Load default conf ###
ADD ooniprobe.conf /var/lib/ooni/

# EXPOSE PORT (For Web UI)
EXPOSE 8842

# Define default command.
CMD /usr/local/bin/ooniprobe-agent run
