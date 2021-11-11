
FROM centos:centos6

MAINTAINER hays.clark@gmail.com

# Install the minimal requirements for Backburner 2014
RUN yum update -y && yum install -y \
    php \
    httpd \
    tcsh \
    glibc.i686 \
    libgcc.i686 \
    libstdc++.i686 \
    libuuid.i686 \
    wget && \
    yum clean all

# Download and unpack distribution first, Docker's caching
# mechanism will ensure that this only happens once.
ARG MAYA_URL=http://download.autodesk.com/us/support/files/maya_2014_service_pack4/Autodesk_Maya_2014sp4_English_Linux_64bit.gz
ARG TEMP_PATH=/tmp/maya
RUN mkdir -p $TEMP_PATH && cd $TEMP_PATH && \
    wget --progress=bar:force $MAYA_URL && \
    tar -zxvf *.gz && rm *.gz && \
    rpm -Uvhi *backburner.monitor*.rpm *base*.rpm *webmonitor*.rpm && \
    rm -rf ${TEMP_PATH}

# CREATE missing file that caused Web service error.
RUN mkdir /usr/discreet/cfg 
COPY network.cfg.sample /usr/discreet/cfg/network.cfg.sample
COPY backburner_docker /tmp/backburner_docker
ARG BB_DOCKER=/etc/rc.d/init.d/backburner_docker
RUN cat /tmp/backburner_docker > $BB_DOCKER && \
    chown root:root $BB_DOCKER && \
    chmod 755 $BB_DOCKER && \
    chkconfig --add backburner_docker && \
    chkconfig --level 345 backburner_docker on

RUN sed -i '/backburner_general/a\\n# Source Backburner general functions and definitions\n. /etc/init.d/backburner_docker' /etc/init.d/backburner_manager

# Disable IPv6
RUN echo "net.ipv6.conf.all.disable_ipv6 = 1" >> /etc/sysctl.conf && \
    echo "net.ipv6.conf.default.disable_ipv6 = 1" >> /etc/sysctl.conf

# Set the workspace to boackburners home
WORKDIR /usr/discreet/backburner

# Web portal volumes
VOLUME ["/etc/httpd/auth/", "/etc/httpd/conf"]

# WWW Port
EXPOSE 80

# Manager Port
EXPOSE 3234
EXPOSE 3234/udp

# Server Port
EXPOSE 3233
EXPOSE 3233/udp

# Job submission from Maya
EXPOSE 7347
EXPOSE 7347/udp

# For the ping pong process and going down if the port is blocked
EXPOSE 29000-30000/udp

# Open ports 45000-65000 to TCP and UDP traffic between the BB Manager and the render nodes if receiving random denials.
# REF: https://knowledge.autodesk.com/support/3ds-max/troubleshooting/caas/sfdcarticles/sfdcarticles/Backburner-Network-Port-Configuration.html
EXPOSE 45000-65000
EXPOSE 45000-65000/udp

# Start container in "Machine mode"
CMD /sbin/init
