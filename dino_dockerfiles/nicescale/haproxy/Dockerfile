FROM ubuntu
RUN  apt-get update
RUN  DEBIAN_FRONTEND=noninteractive apt-get -y install make gcc libssl-dev
ADD  . /opt/nicedocker
RUN  cd /opt/nicedocker/src && make TARGET=linux2628 USE_OPENSSL=1 && make PREFIX=/usr/local/haproxy install
ADD  myssl.pem /etc/ssl/myssl.pem
ADD  haproxy.cfg /etc/haproxy/haproxy.cfg

EXPOSE  80 443
CMD  ["/opt/nicedocker/run.sh"]
