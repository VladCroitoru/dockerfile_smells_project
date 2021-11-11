FROM debian:jessie
MAINTAINER TeKrop <contact@tekrop.fr>

ENV DEBIAN_FRONTEND noninteractive

RUN touch /etc/timezone \
    && /bin/echo -e 'Europe/Paris' > /etc/timezone \
    && dpkg-reconfigure --frontend noninteractive tzdata \
    && sed -i 's,http://httpredir.debian.org/debian,http://debian.mirrors.ovh.net/debian/,g' /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends apt-transport-https apt-utils ca-certificates cron unzip vim wget \
    && rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*

RUN apt-get update \
    && apt-get install -y curl \
    && curl -sL https://deb.nodesource.com/setup_7.x | bash - \
    && apt-get install -y --no-install-recommends nodejs build-essential git

RUN cd /opt/ \
    && git clone https://github.com/TeKrop/lastbustan.git \
    && cd lastbustan \
    && npm install \
    && npm install -g bower \
    && bower install --allow-root \
    && rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*

RUN npm install -g nodemon

EXPOSE 80 443

WORKDIR /opt/lastbustan
CMD ["nodemon", "server.js"]
