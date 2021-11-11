FROM java:8
MAINTAINER Chernov Artur

# 'snapshot' or 'release'
ENV XD_BUILD RELEASE
ENV XD_VERSION 1.3.1.${XD_BUILD}

RUN groupadd -r springxd && useradd -r -g springxd springxd

# Install requiered dependencies
#RUN sudo yum install -y net-tools
#RUN sudo yum install -y curl
#RUN sudo yum install -y rsync
#RUN sudo yum install -y wget
#RUN sudo yum install -y zip unzip

RUN wget http://repo.spring.io/libs-release/org/springframework/xd/spring-xd/${XD_VERSION}/spring-xd-${XD_VERSION}-dist.zip \
      -O /opt/spring-xd-${XD_VERSION}-dist.zip \
    && unzip /opt/spring-xd-${XD_VERSION}-dist.zip -d /opt/ \
    && rm /opt/spring-xd-${XD_VERSION}-dist.zip \
    && /opt/spring-xd-${XD_VERSION}/zookeeper/bin/install-zookeeper \
    && chown -R springxd:springxd /opt/spring-xd-${XD_VERSION} \
    && ln -s /opt/spring-xd-${XD_VERSION} /opt/spring-xd


USER springxd

RUN mkdir /opt/spring-xd-${XD_VERSION}/xd/data \
      && mkdir /opt/spring-xd-${XD_VERSION}/xd/custom-modules

WORKDIR /opt/spring-xd
