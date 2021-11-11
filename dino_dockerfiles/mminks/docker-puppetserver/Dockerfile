FROM debian:jessie

MAINTAINER Meik Minks <docbrown@datenschleuder.org>

# system Upgrade
RUN apt-get update && \
    apt-get -y dist-upgrade

# install required packages
RUN apt-get -y install wget

# install Puppet Collection
RUN wget -q https://apt.puppetlabs.com/puppetlabs-release-pc1-jessie.deb -O /tmp/puppetlabs-release-pc1-jessie.deb && \
    dpkg -i /tmp/puppetlabs-release-pc1-jessie.deb && \
    apt-get update && \
    apt-get -y install puppetserver

# Cleanup
RUN apt-get -y autoremove --purge && \
    apt-get -y autoclean

VOLUME [ "/var/log/puppetlabs", "/etc/puppetlabs/code" ]

EXPOSE 8140

COPY entrypoint.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/entrypoint.sh && \
    ln -s /usr/local/bin/entrypoint.sh /entrypoint.sh

CMD entrypoint.sh
