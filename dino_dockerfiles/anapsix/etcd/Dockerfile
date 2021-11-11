FROM  scratch

ENV ETCD_RELEASE=2.3.0

COPY etcd-v${ETCD_RELEASE}-linux-amd64/etcd etcd-v${ETCD_RELEASE}-linux-amd64/etcdctl /bin/

VOLUME ["/data"]

EXPOSE 4001 7001 2379 2380

ENTRYPOINT ["/bin/etcd"]

CMD ["--data-dir=/data"]
