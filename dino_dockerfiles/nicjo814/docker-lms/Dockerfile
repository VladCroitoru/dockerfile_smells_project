FROM phusion/baseimage

# Set environment variables
ENV DEBIAN_FRONTEND noninteractive
ENV HOME="/root"
ENV TERM=xterm
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8
ENV MEDIASERVER_URL=http://downloads-origin.slimdevices.com/nightly/7.9/sc/3c4e99a/logitechmediaserver_7.9.0~1445336105_all.deb

COPY init/20adduser.sh /etc/my_init.d/20adduser.sh
COPY init/30lms.sh /etc/my_init.d/30lms.sh

RUN apt-get update && apt-get -y install \
        curl \
        faad \
        flac \
        lame \
        sox \
        wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    curl -Lsf -o /tmp/logitechmediaserver.deb $MEDIASERVER_URL && \
    dpkg -i /tmp/logitechmediaserver.deb && \
    rm -f /tmp/logitechmediaserver.deb && \
    useradd -u 911 -U -s /bin/false abc && \
    usermod -G users abc && \
    mkdir -p /config && \
    mkdir -p /music && \
    chmod +x /etc/my_init.d/20adduser.sh && \
    chmod +x /etc/my_init.d/30lms.sh

VOLUME /config
VOLUME /music
EXPOSE 3483 9000 9090

CMD ["/sbin/my_init"]
