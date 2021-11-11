FROM centos:7

MAINTAINER Tapjoy Operations

ADD http://s3.amazonaws.com/downloads.basho.com/riak/2.1/2.1.4/rhel/7/riak-2.1.4-1.el7.centos.x86_64.rpm /tmp/
ADD entrypoint.sh /

# Install riak, set it up to accept external connections
RUN yum install -y /tmp/riak-2.1.4-1.el7.centos.x86_64.rpm \
  && sed -i s/'listener.http.internal = 127.0.0.1:8098'/'listener.http.internal = 0.0.0.0:8098'/g /etc/riak/riak.conf \
  && sed -i s/'listener.protobuf.internal = 127.0.0.1:8087'/'listener.protobuf.internal = 0.0.0.0:8087'/g /etc/riak/riak.conf \
  && rm /tmp/*

EXPOSE 8087 8098
ENTRYPOINT ["/entrypoint.sh"]
