FROM opensuse

MAINTAINER Gyula Voros <gyulavoros87@gmail.com>

ENV WORKBENCH_VERSION couchbase-query-workbench_dp2-linux_x86_64.tar.gz

RUN zypper -n in tar wget \
  && wget -q -P /opt/ http://packages.couchbase.com/releases/query-workbench/dp2/$WORKBENCH_VERSION \
  && cd /opt \
  && tar -zxf $WORKBENCH_VERSION \
  && rm -rf $WORKBENCH_VERSION \
  && zypper -n rm tar wget \
  && zypper clean

ENV GUI_PORT=:8094 COUCHBASE_URL=http://127.0.0.1:8091 USER= PASS=

ADD docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]