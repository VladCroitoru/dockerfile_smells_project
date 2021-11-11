From centos:7

ENV MONGODB_VERSION=3.6 \
    MONGODB_PORT=30000 \
    MONGODB_BIND_IP=0.0.0.0 \
    MONGODB_DPATH="/var/lib/mongo" \
    MONGODB_REPLICA_SET_NAME="replicaset"

COPY mongodb-enterprise-$MONGODB_VERSION.repo /etc/yum.repos.d/mongodb-enterprise.repo

RUN yum install -y mongodb-enterprise

USER mongod

CMD /bin/mongod --port $MONGODB_PORT --bind_ip $MONGODB_BIND_IP --dbpath $MONGODB_DPATH --replSet $MONGODB_REPLICA_SET_NAME
