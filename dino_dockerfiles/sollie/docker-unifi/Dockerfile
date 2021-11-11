FROM lsiobase/xenial

# set version label
ARG BUILD_DATE
ARG VERSION
LABEL build_version="${VERSION} Build-date:- ${BUILD_DATE}"

# package versions
ARG UNIFI_VER="6.0.43"

# environment settings
ARG DEBIAN_FRONTEND="noninteractive"

# add mongo repo
RUN curl -o /tmp/key.asc https://www.mongodb.org/static/pgp/server-3.6.asc && \
    apt-key add /tmp/key.asc && \
    echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" >> /etc/apt/sources.list.d/mongodb-org-3.6.list && \
    apt-get update && \
    apt-get install -y apt-transport-https && \
    apt-get install -y logrotate binutils jsvc mongodb-org-server openjdk-8-jre-headless \
    wget && \
    curl -o /tmp/unifi.deb -L "http://dl.ubnt.com/unifi/${UNIFI_VER}/unifi_sysvinit_all.deb" && \
    dpkg -i /tmp/unifi.deb && \
    apt-get clean && \
    rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*

# add local files
COPY root/ /

#RUN mv /usr/lib/unifi/webapps/ROOT/app-unifi/css /config/css
#RUN ln -sf /config/css /usr/lib/unifi/webapps/ROOT/app-unifi/css

# Volumes and Ports
WORKDIR /usr/lib/unifi
VOLUME /config
EXPOSE 3478/udp 8080 8081 8443 8843 8880
