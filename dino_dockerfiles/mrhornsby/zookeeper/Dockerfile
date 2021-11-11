FROM java:8-jre
MAINTAINER Mark Hornsby <docker@markhornsby.uk>

ARG VERSION=3.5.2-alpha

LABEL name="zookeeper" version=$VERSION

RUN wget -q -O - http://mirror.ox.ac.uk/sites/rsync.apache.org/zookeeper/zookeeper-$VERSION/zookeeper-$VERSION.tar.gz | tar -xzf - -C /opt \
    && ln -s /opt/zookeeper-$VERSION /opt/zookeeper

EXPOSE 2181 2888 3888

WORKDIR /opt/zookeeper

COPY zoo.cfg conf/

COPY entrypoint.sh bin/

RUN chmod a+x bin/entrypoint.sh

ENTRYPOINT ["bin/entrypoint.sh"]

CMD ["1"]
