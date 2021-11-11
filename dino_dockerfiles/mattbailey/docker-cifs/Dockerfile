FROM phusion/baseimage

RUN apt-get update -qq && \
    apt-get -qqy install samba && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /etc/service/smbd /etc/service/nmbd
ADD smbd.sh etc/service/smbd/run
ADD nmbd.sh etc/service/nmbd/run
ADD samba.sh samba.sh

EXPOSE 139
EXPOSE 445

ENTRYPOINT ["/samba.sh"]
