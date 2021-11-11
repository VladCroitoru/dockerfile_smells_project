FROM alpine:3.2
RUN  apk add --update ca-certificates openssl tar && \
     wget https://github.com/coreos/etcd/releases/download/v3.1.6/etcd-v3.1.6-linux-amd64.tar.gz && \
     tar xzvf etcd-v3.1.6-linux-amd64.tar.gz && \
     mv etcd-v3.1.6-linux-amd64/etcd* /bin/ && \
     apk del --purge tar openssl && \
     rm -Rf etcd-v3.1.6-linux-amd64* /var/cache/apk/*
ADD run.sh /bin/run.sh
RUN chmod +x /bin/run.sh
VOLUME ["/var/etcd/data", "/etc/etcd/ssl", "/etc/ca/ssl"]
EXPOSE 2379 2380 4001 
ENTRYPOINT  ["/bin/run.sh"]
