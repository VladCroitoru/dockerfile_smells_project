FROM qnib/alplain-jre8

# inspired by
# https://github.com/HariSekhon/Dockerfiles/tree/hbase-1.2/hbase

ARG HBASE_VERSION=1.3.1
ARG HBASE_URL=https://archive.apache.org/dist/hbase
ENV PATH=$PATH:/opt/hbase/bin \
    HBASE_CONF_DIR=/hbase/conf/ \
    HBASE_REGIONSERVERS=localhost \
    ZK_HOST=tasks.zookeeper \
    HBASE_MANAGES_ZK=false \
    ENTRYPOINTS_DIR=/opt/qnib/entry

VOLUME ["/tmp/hbase-root/"]
RUN apk add --no-cache bash wget tar \
 && wget -qO- "${HBASE_URL}/${HBASE_VERSION}/hbase-${HBASE_VERSION}-bin.tar.gz" |tar xfz - -C /opt/ \
 && mv /opt/hbase-${HBASE_VERSION} /opt/hbase/
COPY conf/hbase-site.xml /opt/qnib/hbase/conf/
COPY opt/qnib/entry/25-hbase-zk.sh \
     opt/qnib/entry/30-hbase-master.sh \
     opt/qnib/entry/31-hbase-regionserver.sh \
     opt/qnib/entry/32-hbase-rest.sh \
     opt/qnib/entry/33-hbase-thrift.sh \
     opt/qnib/entry/40-wait-for-hbase.sh \
     /opt/qnib/entry/
COPY opt/qnib/hbase/bin/tail.sh /opt/qnib/hbase/bin/
COPY opt/qnib/hbase/scripts/create_emp /opt/qnib/hbase/scripts/
RUN echo "hbase shell /opt/qnib/hbase/scripts/create_emp" >> /root/.bash_history
CMD /opt/qnib/hbase/bin/tail.sh
