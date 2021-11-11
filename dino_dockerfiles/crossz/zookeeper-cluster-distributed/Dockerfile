FROM centos:7
MAINTAINER Cross Zheng

ARG CLIENTPORT=2181
ARG MIRROR=http://archive.apache.org/dist
ARG VERSION=3.4.8

LABEL name="zookeeper" version=$VERSION

# https://github.com/Yelp/dumb-init
RUN curl -fLsS -o /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.0.2/dumb-init_1.0.2_amd64 && chmod +x /usr/local/bin/dumb-init

RUN yum install -y java-1.7.0-openjdk-headless tar

# https://www.apache.org/mirrors/dist.html
RUN curl -fL $MIRROR/zookeeper/zookeeper-$VERSION/zookeeper-$VERSION.tar.gz | tar xzf - -C /opt && \
mv /opt/zookeeper-$VERSION /opt/zookeeper

VOLUME /tmp/zookeeper

COPY entrypoint.sh /

ENTRYPOINT ["/usr/local/bin/dumb-init", "/entrypoint.sh"]

ENV PATH $PATH:/opt/zookeeper/bin
EXPOSE $CLIENTPORT

CMD ["zkServer.sh", "start-foreground"]
