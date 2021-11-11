FROM nimbix/centos-desktop
MAINTAINER Nimbix, Inc.

RUN yum install -y wget java-1.8.0-openjdk-headless.x86_64 && yum clean all
RUN yum install -y boost-devel \
    libxml2-devel \
    make openssl-devel \
    rpm-build \
    git \
    vixie-cron && \
    yum groupinstall -y 'Development Tools' && \
    yum clean all

VOLUME /tmp
WORKDIR /tmp

RUN git clone -b 6.0.2 https://github.com/adaptivecomputing/torque.git && \
    cd /tmp/torque && \
    ./autogen.sh && \
     ./configure && \
     make rpm && \
     cp -r /root/rpmbuild/RPMS/x86_64 /tmp/PKG && \
     rm -rf /root/rpmbuild/RPMS/x86_64 && \
     cd /tmp/PKG && \
     rpm -ivh *.rpm && \
     rm -rf *.rpm

RUN wget "https://github.com/marbl/canu/releases/download/v1.4/canu-1.4.Linux-amd64.tar.xz" && tar xvf canu-1.4.Linux-amd64.tar.xz && mv /tmp/canu-1.4 /usr/local/canu-1.4

ADD ./scripts /usr/local/scripts/torque
ADD ./scripts /usr/local/scripts/canu
ADD ./NAE/AppDef.json /etc/NAE/AppDef.json
ADD ./NAE/AppDef.png /etc/NAE/AppDef.png
ADD ./NAE/help.html /etc/NAE/help.html
COPY ./NAE/screenshot.png /etc/NAE/screenshot.png

CMD ["/usr/local/scripts/canu/canu-pipeline.sh"]
