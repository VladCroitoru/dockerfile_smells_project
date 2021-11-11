FROM starase/base
MAINTAINER Paolo De Michele <paolo@starase.com>

RUN apt update -y \
    && curl -O https://apt.puppetlabs.com/puppetlabs-release-pc1-xenial.deb \
    && dpkg -i puppetlabs-release-pc1-xenial.deb \
    && apt update -y \
    && apt install puppetserver -y

COPY default/puppetserver /etc/default/
COPY supervisor/puppetserver.conf /etc/supervisor/conf.d/

RUN rm -rf puppetlabs-release-pc1-xenial.deb 

WORKDIR /opt/puppetlabs/
EXPOSE 8140
