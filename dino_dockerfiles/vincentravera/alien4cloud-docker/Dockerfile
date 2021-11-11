FROM ubuntu:trusty

LABEL maintainer Vincent RAVERA <ravera.vincent@gmail.com>

RUN apt-get update

WORKDIR /root/

# Alien4Cloud prerequisites
# Misc
RUN apt-get install -y curl wget git python python3

# JAVA
COPY jre-8u161-linux-x64.tar.gz /opt/
RUN cd /opt/; tar -zxvf jre-8u161-linux-x64.tar.gz
ENV JAVA_HOME="/opt/jre1.8.0_161/"

# Docker
RUN apt-get install -y apt-transport-https ca-certificates software-properties-common
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
RUN apt-get update
RUN apt-get install -y docker-ce

# Alien4cloud
COPY start_alien4cloud.sh /root/

ENV ALIEN4CLOUD_VERSION=1.4.3.1
ENV FASTCONNECT_REPOSITORY=opensource
ENV INSTALL=/root/alien4cloud-getstarted

RUN mkdir -p $INSTALL

RUN cd $INSTALL && curl -k -o "alien4cloud-dist-${ALIEN4CLOUD_VERSION}.tar.gz" -L "http://fastconnect.org/maven/service/local/artifact/maven/redirect?r=$FASTCONNECT_REPOSITORY&g=alien4cloud&a=alien4cloud-dist&v=${ALIEN4CLOUD_VERSION}&p=tar.gz&c=dist"


RUN cd $INSTALL &&  curl -k -o "puccini-cli-${ALIEN4CLOUD_VERSION}.tgz" -L "http://fastconnect.org/maven/service/local/artifact/maven/redirect?r=$FASTCONNECT_REPOSITORY&g=org.alien4cloud.puccini&a=puccini-cli&v=${ALIEN4CLOUD_VERSION}&p=tgz"

RUN cd $INSTALL &&  curl -k -o "alien4cloud-puccini-plugin-${ALIEN4CLOUD_VERSION}.zip" -L "http://fastconnect.org/maven/service/local/artifact/maven/redirect?r=$FASTCONNECT_REPOSITORY&g=alien4cloud&a=alien4cloud-puccini-plugin&v=${ALIEN4CLOUD_VERSION}&p=zip"

RUN cd $INSTALL ; tar zxvf alien4cloud-dist-${ALIEN4CLOUD_VERSION}.tar.gz

RUN cd $INSTALL ; tar xvzf puccini-cli-${ALIEN4CLOUD_VERSION}.tgz

ENV PUCCINI_DIR=puccini-cli-${ALIEN4CLOUD_VERSION}

RUN cd $INSTALL ; mv alien4cloud-puccini-plugin-${ALIEN4CLOUD_VERSION}.zip alien4cloud/init/plugins/

COPY start_alien4cloud.sh /root/

# RUN rm alien4cloud-dist-${ALIEN4CLOUD_VERSION}.tar.gz
# RUN rm puccini-cli-${ALIEN4CLOUD_VERSION}.tgz

VOLUME /var/run/docker
VOLUME /var/run/docker.sock

EXPOSE 8088

CMD bash start_alien4cloud.sh











