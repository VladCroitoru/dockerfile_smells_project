FROM centos:6
MAINTAINER Adrian Oprea<adrian@codesi.nz>

RUN rpm --import https://getfedora.org/static/0608B895.txt
RUN yum update -y && yum install -y tar python-setuptools
RUN easy_install supervisor

RUN mkdir -p /var/log/supervisor
COPY conf/supervisord.conf /etc/supervisord.conf

WORKDIR /tmp
RUN curl -O http://download.macromedia.com/pub/adobemediaserver/5_0_8/AdobeMediaServer5_x64.tar.gz
WORKDIR /tmp/ams_latest
RUN tar zxvf ../AdobeMediaServer5_x64.tar.gz -C . --strip-components=1
RUN rm -Rf License.txt
RUN sed -i -e 's:read cont < /dev/tty:#read cont < /dev/tty:g' installAMS

COPY conf/installAMS.input installAMS.input

RUN ./installAMS < installAMS.input
COPY certs /opt/adobe/certs
COPY conf/Adaptor.xml /opt/adobe/ams/conf/_defaultRoot_/Adaptor.xml

# CLEANUP
WORKDIR /tmp
RUN rm -Rf ams_latest AdobeMediaServer5_x64.tar.gz

VOLUME ["/opt/adobe/ams/applications"]

EXPOSE 80 443 1111 1935

CMD ["/usr/bin/supervisord"]
