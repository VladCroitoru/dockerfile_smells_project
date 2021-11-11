FROM alpine:3.6

RUN apk add --no-cache ca-certificates openssl

ENV RANCHER_GEN_RELEASE=v0.6.0 \
    RGON_EXEC_RELEASE=v1.1.1 \
    ACMETOOL_RELEASE=v0.0.59

# Consider revising: https://www.ctl.io/developers/blog/post/dockerfile-add-vs-copy/#which-to-use
ADD https://github.com/causticlab/go-rancher-gen/releases/download/${RANCHER_GEN_RELEASE}/rancher-gen-linux-amd64.tar.gz /tmp/rancher-gen.tar.gz
ADD https://github.com/causticlab/rgon-exec/releases/download/${RGON_EXEC_RELEASE}/rgon-exec-linux-amd64.tar.gz /tmp/rgon-exec.tar.gz
ADD https://github.com/hlandau/acme/releases/download/${ACMETOOL_RELEASE}/acmetool-${ACMETOOL_RELEASE}-linux_amd64.tar.gz /tmp/acmetool.tar.gz

RUN ls /tmp/*.tar.gz | xargs -i tar zxf {} -C /usr/local/bin

RUN mv /usr/local/bin/acmetool-${ACMETOOL_RELEASE}-linux_amd64/bin/acmetool /usr/local/bin/acmetool \
 && mv /usr/local/bin/rgon-exec-linux-amd64 /usr/local/bin/rgon-exec

COPY app/acmetool/hooks/01copyCertsToNginx.sh  /usr/lib/acme/hooks/
COPY app/cron/daily/acmetool-cron /etc/periodic/daily/
COPY examples/rancher-gen/ /app/rancher-gen/default/
COPY examples/acmetool/ /app/acme/conf/
COPY app/entrypoint.sh /app/

RUN chmod +x /usr/local/bin/rancher-gen \
    && chmod +x /usr/local/bin/rgon-exec \
    && chmod +x /usr/local/bin/acmetool \
    && chown root:root /usr/local/bin/* \
    && chmod +x /app/* \
    && chown root:root /usr/lib/acme/hooks/* \
    && chmod +x /usr/lib/acme/hooks/* \
    && chmod +x /etc/periodic/daily/* \
    && rm /tmp/*.tar.gz

ENTRYPOINT ["/bin/sh", "/app/entrypoint.sh" ]
CMD ["rancher-gen", "--config", "/etc/rancher-gen/default/rancher-gen.cfg"]