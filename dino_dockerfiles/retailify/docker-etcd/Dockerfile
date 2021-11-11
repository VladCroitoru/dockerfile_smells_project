FROM        alpine:3.4
ENV VERSION 3.0.4
RUN         apk add --update ca-certificates openssl tar && \
	    wget https://github.com/coreos/etcd/releases/download/v${VERSION}/etcd-v${VERSION}-linux-amd64.tar.gz && \
            tar xzvf etcd-v${VERSION}-linux-amd64.tar.gz && \
            mv etcd-v${VERSION}-linux-amd64/etcd* /bin/ && \
            apk del --purge tar openssl && \
            rm -Rf etcd-v${VERSION}-linux-amd64* /var/cache/apk/*
VOLUME      /data
EXPOSE      2379 2380 4001 7001
ADD         run.sh /bin/run.sh
ENTRYPOINT  ["/bin/run.sh"]
