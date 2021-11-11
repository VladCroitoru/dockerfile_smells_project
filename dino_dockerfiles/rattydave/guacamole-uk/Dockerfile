FROM ubuntu:18.04

EXPOSE 8080
VOLUME /etc/guacamole
VOLUME /file-transfer

ENV VERSION=1.2.0
WORKDIR /APP/bin/remote


RUN apt-get update && apt-get install -y \
    automake \
    build-essential \
    checkinstall \
    libavcodec-dev \
    libavutil-dev \
    libcairo2-dev \
    libfreerdp-dev \
    libossp-uuid-dev \
    libpango1.0-dev \
    libpng-dev \
    libpulse-dev \
    libssh2-1-dev \
    libssl-dev \
    libswscale-dev \
    libtelnet-dev \
    libvncserver-dev \
    libvorbis-dev \
    libwebp-dev \
    man-db \
    tomcat8 \
    wget \
    && rm -rf /var/lib/apt/lists/* \
    && wget "http://archive.apache.org/dist/guacamole/${VERSION}/source/guacamole-server-${VERSION}.tar.gz" \
    && tar zxvf guacamole-server-${VERSION}.tar.gz \
    && cd /APP/bin/remote/guacamole-server-${VERSION}/src/protocols/rdp \
    && cd /APP/bin/remote/guacamole-server-${VERSION} \
    && ./configure --with-init-dir=/etc/init.d \
    && make -j$(nproc) \
    && make install \
    && ldconfig  \
    && mkdir /usr/lib/x86_64-linux-gnu/freerdp \
    && ln -s /usr/local/lib/freerdp/*.so /usr/lib/x86_64-linux-gnu/freerdp/. \
    && cd /APP/bin/remote \
    && wget http://archive.apache.org/dist/guacamole/${VERSION}/binary/guacamole-${VERSION}.war \
    && ln -s /APP/bin/remote/guacamole-${VERSION}.war /var/lib/tomcat8/webapps/remote.war \
    && echo "GUACAMOLE_HOME=/etc/guacamole" >> /etc/default/tomcat8 \
    && chown tomcat8:tomcat8 /file-transfer \
    && apt-get -y autoclean && apt-get -y autoremove \
    && apt-get -y purge $(dpkg --get-selections | grep deinstall | sed s/deinstall//g) \
    && rm -rf /var/lib/apt/lists/*

COPY start.sh /tmp/start.sh

ENTRYPOINT ["/bin/bash"]
CMD ["/tmp/start.sh"]
