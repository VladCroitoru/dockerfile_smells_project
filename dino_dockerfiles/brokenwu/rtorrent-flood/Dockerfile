#Dockerfile rtorrent-flood
FROM tlnk/ubuntu:latest
MAINTAINER tlnk <support@tlnk.fr>

ARG VERSION
ARG BUILD_DATE
ARG VCS_REF
ARG RTORRENT_VERSION
ARG LIBTORRENT_VERSION

EXPOSE 3000
EXPOSE 5000
EXPOSE 55950-56000
EXPOSE 6881

#Install packages
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - && \ 
    apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y \
    git \
    build-essential \
    subversion \
    autoconf \
    screen \
    g++ \
    gcc \
    ntp \
    curl \
    comerr-dev \
    pkg-config \
    cfv \
    libtool \
    libssl-dev \
    libncurses5-dev \
    ncurses-term \
    libsigc++-2.0-dev \
    libcppunit-dev \
    libcurl3 \
    libcurl4-openssl-dev




#Setup xmlrpc & libtorrent & rtorrent
RUN svn co -q https://svn.code.sf.net/p/xmlrpc-c/code/stable /tmp/xmlrpc-c && \
    cd /tmp/xmlrpc-c && \
    ./configure --disable-libwww-client --disable-wininet-client --disable-abyss-server --disable-cgi-server && \
    make -j2 && \
    make install && \
    cd /tmp && \
    curl http://rtorrent.net/downloads/libtorrent-$LIBTORRENT_VERSION.tar.gz | tar xz && \
    cd libtorrent-$LIBTORRENT_VERSION && \
    ./autogen.sh && \
    ./configure && \
    make -j2 && \
    make install && \
    cd /tmp && \
    curl http://rtorrent.net/downloads/rtorrent-$RTORRENT_VERSION.tar.gz | tar xz && \
    cd rtorrent-$RTORRENT_VERSION && \
    ./autogen.sh && \
    ./configure --with-xmlrpc-c && \
    make -j2 && \
    make install && \
    ldconfig && \
    mkdir -p /downloads/{.session,~watch} && \
    chown -R root:root /downloads

#Setup flood    
RUN git clone https://github.com/jfurrow/flood.git /var/www/flood && \
    cd /var/www/flood && \
    cp config.template.js config.js


COPY entrypoint /entrypoint
COPY .rtorrent.rc /root/.rtorrent.rc
COPY rtorrent /etc/init.d/rtorrent

#Setup NPM
RUN apt-get install -y nodejs && \
    npm cache clean -f && \
    npm install -g n && \
    n 6.9.5 && \
    cd /var/www/flood && \
    npm install --production

#Last config + clean
RUN chmod +x /etc/init.d/rtorrent && \
    update-rc.d rtorrent defaults && \
    chmod +x /entrypoint/*sh && \
    chmod +x /entrypoint/entrypoint.d/*.sh && \
    apt-get clean && \
    rm -rf /tmp/*


WORKDIR /var/www/flood

ENTRYPOINT ["/bin/bash", "/entrypoint/entrypoint.sh"]
CMD [ "npm", "start" ]

LABEL org.label-schema.version=$VERSION
LABEL org.label-schema.build-date=$BUILD_DATE
LABEL org.label-schema.vcs-ref=$VCS_REF
LABEL org.label-schema.vcs-url="https://github.com/tle06/rtorrent-flood.git"
LABEL org.label-schema.name="rtorrent-flood"
LABEL org.label-schema.vendor="rtorrent-flood"
LABEL org.label-schema.schema-version="1.0"