FROM mengbo/docker-dnscrypt

MAINTAINER Meng Bo "mengbo@lnu.edu.cn"

RUN echo "deb http://cn.archive.ubuntu.com/ubuntu trusty main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get -y install curl
RUN apt-get -y install python python-dev
RUN apt-get -y install libevent-dev
RUN apt-get -y install python-gevent python-openssl python-crypto

RUN apt-get -y install python-pip
RUN pip install dnslib

RUN mkdir -p /usr/local/src;\
  cd /usr/local/src;\
  curl https://nodeload.github.com/goagent/goagent/legacy.tar.gz/3.0 | tar xz;\
  mv goagent* goagent;\
  mkdir -p /opt/goagent;\
  cp -r /usr/local/src/goagent/local /opt/goagent;\
  rm -f /opt/goagent/local/CA.crt;\
  cp -r /usr/local/src/goagent/server /opt/goagent

RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8 

ADD startlocal.sh /opt/goagent/startlocal
RUN chmod +x /opt/goagent/startlocal
ADD uploadserver.sh /opt/goagent/uploadserver
RUN chmod +x /opt/goagent/uploadserver
ADD run.sh /run.sh
RUN chmod +x /run.sh
ADD proxy.user.ini /opt/goagent/local/proxy.user.ini


VOLUME ["/usr/local/share/ca-certificates"]

EXPOSE 8087

CMD ["/run.sh"]
