FROM debian:jessie

COPY init.sh /etc/init.sh

RUN apt-get update && apt-get install -y wget \
    && wget -O - http://download.gluster.org/pub/gluster/glusterfs/3.7/3.7.9/rsa.pub | apt-key add - \
    && echo deb http://download.gluster.org/pub/gluster/glusterfs/3.7/3.7.9/Debian/jessie/apt jessie main > /etc/apt/sources.list.d/gluster.list \
    && apt-get update && apt-get -y install glusterfs-server glusterfs-client attr && apt-get clean \
    && chmod a+x /etc/init.sh

ENV GLUSTERVOLNAME data
EXPOSE 111 245 443 24007 24008 24009 24010 24011 24012 24013 24014 24015 2049 8080 6010 6011 6012 38465 38466 38468 38469 49152 49153 49154 49156 49157 49158 49159 49160 49161 49162 49163

CMD ["/etc/init.sh"]
