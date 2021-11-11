FROM node:10

LABEL maintainer="Erin Schnabel <ebullient@redhat.com> (@ebullientworks)"

RUN wget https://github.com/coreos/etcd/releases/download/v2.2.2/etcd-v2.2.2-linux-amd64.tar.gz -q && \
    tar xzf etcd-v2.2.2-linux-amd64.tar.gz etcd-v2.2.2-linux-amd64/etcdctl --strip-components=1 && \
    rm etcd-v2.2.2-linux-amd64.tar.gz && \
    mv etcdctl /usr/local/bin/etcdctl

ADD . /srv/www
WORKDIR /srv/www

RUN npm install -d --unsafe-perm --production

EXPOSE 3000

CMD ./bin/startup.sh
