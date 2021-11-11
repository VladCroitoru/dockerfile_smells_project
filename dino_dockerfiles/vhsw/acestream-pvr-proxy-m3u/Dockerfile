FROM ubuntu:latest

## env vars
ENV DEBIAN_FRONTEND noninteractive 
ENV SUPERVISORD_CONF=/etc/supervisor/supervisord.conf
ENV SUPERVISORD_ACESTREAM_CONF=/etc/supervisor/conf.d/acestream.conf
ENV ACESTREAM_CONF=/etc/acestream

## general bootstrap
RUN apt-get update
RUN apt-get install -y wget gnupg supervisor net-tools

## ace-stream
RUN apt-get install -y libxslt1.1 libpython2.7 python-setuptools python-apsw ffmpeg libssl1.0.0
RUN wget http://mirrors.edge.kernel.org/ubuntu/pool/universe/m/m2crypto/python-m2crypto_0.24.0-2_amd64.deb
RUN dpkg -i python-m2crypto_0.24.0-2_amd64.deb
RUN rm python-m2crypto_0.24.0-2_amd64.deb
RUN wget http://dl.acestream.org/linux/acestream_3.1.16_ubuntu_16.04_x86_64.tar.gz
RUN tar -xzf acestream_3.1.16_ubuntu_16.04_x86_64.tar.gz
RUN rm /acestream_3.1.16_ubuntu_16.04_x86_64.tar.gz 
RUN mv /acestream_3.1.16_ubuntu_16.04_x86_64 /opt/acestream

## ace-proxy
RUN apt-get install -y python2.7 python-gevent python-psutil git
RUN git clone https://github.com/pepsik-kiev/HTTPAceProxy.git


## housekeeping
RUN apt-get remove -y git
RUN apt-get -y autoclean
RUN apt-get -y autoremove
RUN rm -rf /var/lib/apt /var/lib/dpkg /var/lib/cache /var/lib/log /HTTPAceProxy/.git/

## volumes
VOLUME [ "/config" ]
COPY config/supervisor/supervisord.conf ${SUPERVISORD_CONF}
COPY config/supervisor/conf.d/acestream.conf ${SUPERVISORD_ACESTREAM_CONF}
ADD start.sh /usr/bin/start.sh
RUN chmod +x /usr/bin/start.sh

EXPOSE 8000

## let's get the show on the road
ENTRYPOINT ["start.sh"] 