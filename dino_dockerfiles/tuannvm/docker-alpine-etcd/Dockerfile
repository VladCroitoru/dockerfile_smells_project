FROM gliderlabs/alpine
ENV VERSION v3.1.5
RUN  apk add --update ca-certificates openssl tar curl && \
     wget https://github.com/coreos/etcd/releases/download/${VERSION}/etcd-${VERSION}-linux-amd64.tar.gz && \
     tar xzvf etcd-${VERSION}-linux-amd64.tar.gz && \
     mv etcd-${VERSION}-linux-amd64/etcd* /bin/ && \
     apk del --purge tar openssl && \
     rm -Rf etcd-${VERSION}-linux-amd64* /var/cache/apk/*
VOLUME /data
EXPOSE 2379 2380
CMD [/bin/sh]
