FROM gcr.io/etcd-development/etcd:v3.2.13
FROM traefik:v1.5.0


FROM alpine

# Supervisor
RUN apk --no-cache add supervisor
COPY supervisord.conf /etc/supervisord.conf

# ETCD
COPY --from=0 /usr/local/bin/etcd /usr/local/bin/
COPY --from=0 /usr/local/bin/etcdctl /usr/local/bin/
RUN mkdir -p /var/etcd/ /var/lib/etcd/
ENV ETCD_NAME="etcd" \
    ETCD_DATA_DIR="/etcd-data" \
    ETCD_INITIAL_CLUSTER_TOKEN="etcd-cluster" \
    ETCD_INITIAL_ADVERTISE_PEER_URLS="https://localhost:2380" \
    ETCD_LISTEN_CLIENT_URLS="https://0.0.0.0:2379" \
    ETCD_ADVERTISE_CLIENT_URLS="https://localhost:2379" \
    ETCD_LISTEN_PEER_URLS="https://0.0.0.0:2380" \
    ETCD_INITIAL_CLUSTER="etcd=https://localhost:2380" \
    ETCD_INITIAL_CLUSTER_STATE="new" \
    ETCD_CERT_FILE="/certs/etcd.crt" \
    ETCD_KEY_FILE="/certs/etcd.key" \
    ETCD_PEER_AUTO_TLS=true \
    ETCD_ENABLE_V2=false \
    ETCDCTL_API=3

# Traefik
COPY --from=1 /traefik /usr/local/bin/
COPY --from=1 /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
RUN mkdir -p /
COPY traefik.toml .

COPY launch.sh .

RUN printf '#!/bin/sh\ntail -f /var/log/* -n 300' > /usr/local/bin/debug && \
    chmod +x /usr/local/bin/debug

VOLUME /etcd-data

EXPOSE 2379 2380 80 443

ENTRYPOINT ["./launch.sh"]
