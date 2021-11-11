## -*- docker-image-name: "mcreations/HockeyKit" -*-

FROM mcreations/openwrt-php5
MAINTAINER Gelareh Abooghadareh <abooghadareh@m-creations.net> 

# HOCKEY Version
ENV HOCKEY_VERSION v20140915
ENV HOCKEY 20140915

RUN mkdir -p /opt/hockeykit && \

# added due to php DOM error and date error 
opkg update && \ 
opkg install --force-checksum php5-mod-dom && \ 
opkg install --force-checksum zoneinfo-core && \

wget -O - https://github.com/m-creations/HockeyKit/archive/${HOCKEY_VERSION}.tar.gz  | tar xzf - -C "/opt/hockeykit"

RUN  cp -r /opt/hockeykit/HockeyKit-${HOCKEY}/server/php/public/*  /usr/share/htdocs && \
cp -r /opt/hockeykit/HockeyKit-${HOCKEY}/server/php/includes/  /usr/share && \
mkdir -p /usr/share/log

# ADD image/root / 


