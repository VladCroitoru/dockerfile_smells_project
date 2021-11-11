FROM nginx:latest

ENV SIAB_USERCSS="Normal:+/etc/shellinabox/options-enabled/00+Black-on-White.css,Reverse:-/etc/shellinabox/options-enabled/00_White-On-Black.css;Colors:+/etc/shellinabox/options-enabled/01+Color-Terminal.css,Monochrome:-/etc/shellinabox/options-enabled/01_Monochrome.css" \
    SIAB_ADDUSER=true \
    SIAB_USER=guest \
    SIAB_USER_COUNT=10 \
    SIAB_USERID=1000 \
    SIAB_GROUP=guest \
    SIAB_GROUPID=1000 \
    SIAB_PASSWORD=putsafepasswordhere \
    SIAB_SHELL=/bin/bash \
    SIAB_HOME=/home/guest \
    SIAB_SUDO=false \
    SIAB_SSL=true \
    SIAB_SERVICE=/:LOGIN \
    SIAB_PKGS=none \
    SIAB_SCRIPT=none

RUN apt-get update && apt-get install -y openssl curl openssh-client sudo shellinabox \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && ln -sf '/etc/shellinabox/options-enabled/00+Black on White.css' \
         /etc/shellinabox/options-enabled/00+Black-on-White.css \
    && ln -sf '/etc/shellinabox/options-enabled/00_White On Black.css' \
         /etc/shellinabox/options-enabled/00_White-On-Black.css \
    && ln -sf '/etc/shellinabox/options-enabled/01+Color Terminal.css' \
         /etc/shellinabox/options-enabled/01+Color-Terminal.css


ARG JMETER_VERSION="5.3"

ENV JMETER_HOME /opt/apache-jmeter-${JMETER_VERSION}
ENV	JMETER_BIN ${JMETER_HOME}/bin
ENV	JMETER_DOWNLOAD_URL https://archive.apache.org/dist/jmeter/binaries/apache-jmeter-${JMETER_VERSION}.tgz

ARG TZ="Asia/Bangkok"
ENV TZ ${TZ}

RUN apt-get update \
    && apt-get install -y openjdk-11-jre tzdata unzip bash \
    && apt-get clean \
 	&& mkdir -p /tmp/dependencies \
 	&& curl -L --silent ${JMETER_DOWNLOAD_URL} >  /tmp/dependencies/apache-jmeter-${JMETER_VERSION}.tgz  \
 	&& mkdir -p /opt  \
 	&& tar -xzf /tmp/dependencies/apache-jmeter-${JMETER_VERSION}.tgz -C /opt  \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
 	&& rm -rf /tmp/dependencies

RUN echo "PATH=$PATH:$JMETER_BIN" >> /etc/profile

VOLUME /etc/shellinabox /var/log/supervisor /home /jmeter-script /reports

ADD example /jmeter-script/

RUN mkdir /reports

COPY assets/00-shellinaboxd-entrypoint.sh /docker-entrypoint.d/

RUN chmod +x /docker-entrypoint.d/00-shellinaboxd-entrypoint.sh

COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf

COPY assets/limits.conf /etc/security/limits.conf

ADD lib ${JMETER_HOME}/lib/ext