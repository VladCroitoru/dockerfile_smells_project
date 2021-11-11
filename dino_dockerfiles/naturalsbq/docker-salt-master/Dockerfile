FROM ubuntu:14.04
MAINTAINER bingqian <naturalsbq@live.cn>

ADD SALTSTACK-GPG-KEY.pub /tmp/SALTSTACK-GPG-KEY.pub

# Run Command
RUN apt-key add /tmp/SALTSTACK-GPG-KEY.pub && \
    rm -f /tmp/SALTSTACK-GPG-KEY.pub && \
    echo "deb http://repo.saltstack.com/apt/ubuntu/14.04/amd64/2016.11 trusty main" >> /etc/apt/sources.list.d/saltstack.list && \
    apt-get -qq -y update && \
    apt-get -qq -y install salt-master && \
    apt-get -qq -y install salt-api && \
    apt-get -qq -y autoremove && \
    apt-get -qq -y clean && \
    rm -rf /var/lib/apt/lists/*

# Volumes
VOLUME ['/etc/salt']

# Ports
EXPOSE 4505 4506

CMD ["/usr/bin/salt-master"]


