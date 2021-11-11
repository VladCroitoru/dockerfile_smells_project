FROM ubuntu:14.04

MAINTAINER Brian Sodano <briansodano@gmail.com>

# Install dependencies
RUN apt-get update && \
    apt-get install -yq runit wget python-httplib2 supervisor && \
    apt-get autoremove && apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV CB_VERSION=4.1.0 \
    CB_RELEASE_URL=http://packages.couchbase.com/releases \
    CB_PACKAGE=couchbase-server-community_4.1.0-ubuntu14.04_amd64.deb \
    QUERY_WORKBENCH_VERSION=dp3 \
    QUERY_WORKBENCH_PACKAGE=couchbase-query-workbench_dp3-linux_x86_64.tar.gz \
    CB_SHA256=400263bd03e32b69259ec9b821bf58922030ba9e2a266e2ef4a0d4ac162188ea \
    PATH=$PATH:/opt/couchbase/bin:/opt/couchbase/bin/tools:/opt/couchbase/bin/install \
    LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/couchbase/lib

# Create Couchbase user with UID 1000 (necessary to match default
# boot2docker UID)
RUN groupadd -g 1000 couchbase && useradd couchbase -u 1000 -g couchbase -M

# Install couchbase, init the cluster and create a default bucket
RUN wget -N $CB_RELEASE_URL/$CB_VERSION/$CB_PACKAGE && \
    echo "$CB_SHA256  $CB_PACKAGE" | sha256sum -c - && \
    dpkg -i ./$CB_PACKAGE && rm -f ./$CB_PACKAGE && \
    sleep 10 && /opt/couchbase/bin/couchbase-cli  cluster-init -c $HOSTNAME:8091 --cluster-username=Administrator  --cluster-password=password --cluster-port=8091 --cluster-ramsize=384 --cluster-index-ramsize=384 --services=data,index,query && /opt/couchbase/bin/couchbase-cli bucket-create -c $HOSTNAME:8091 --bucket=default --bucket-type=couchbase --bucket-port=11211  --bucket-ramsize=100  --bucket-replica=0 -u Administrator -p password

# Add runit script for couchbase-server
COPY scripts/run /etc/service/couchbase-server/run

# Install Query Workbench
RUN wget -N $CB_RELEASE_URL/query-workbench/$QUERY_WORKBENCH_VERSION/$QUERY_WORKBENCH_PACKAGE && \
    tar -zxvf $QUERY_WORKBENCH_PACKAGE && rm -f ./$QUERY_WORKBENCH_PACKAGE

# Add supervisor configuration, wrap queryworkbench call in scripts to allow 5 seconds sleep and let couchbase starts
COPY scripts/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY scripts/queryworkbench.sh /queryworkbench.sh

# Add bootstrap script
COPY scripts/entrypoint.sh /
RUN chmod 755 /entrypoint.sh
RUN chmod 755 /queryworkbench.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["/usr/bin/supervisord"]

EXPOSE 4369 8091 8092 8093 8094 8095 9100 9101 9102 9103 9104 9105 9998 9999 11207 11209 11210 11211 11214 11215 18091 18092 18093
VOLUME /opt/couchbase/var