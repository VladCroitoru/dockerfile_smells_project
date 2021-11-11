FROM ubuntu:xenial

RUN apt-get update &&\
    apt-get install software-properties-common python-software-properties -y &&\
    add-apt-repository ppa:freeradius/stable-3.0 -y &&\
    apt-get update &&\
    apt-get install freeradius freeradius-ldap freeradius-utils ldap-utils samba winbind -y &&\
    update-rc.d nmbd defaults &&\
    update-rc.d smbd defaults &&\
    update-rc.d winbind defaults &&\
    service nmbd start &&\
    service smbd start &&\
    service winbind start &&\
    apt-get clean &&\
    echo "\$INCLUDE dictionary.softonic" >> /usr/share/freeradius/dictionary

ADD rootfs /

EXPOSE 1812/udp 1813/udp 18120/udp

ENTRYPOINT ["/init"]
