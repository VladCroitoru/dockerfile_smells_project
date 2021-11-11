FROM janeczku/alpine-haproxy:1.6.3

#Environment variables
ENV S6_OVERLAY_VERSION="v1.17.1.2" \
    CONSUL_TEMPLATE_VERSION="0.13.0" \
    CONSUL_HOST=172.17.0.1:8500 \
    CONSUL_TEMPLATE_DAEMON_ARGS="-config /config/haproxy.json" \
    HAPROXY_DAEMON_ARGS="-D -f /config/haproxy.cfg -p /var/run/haproxy.pid" \
    S6_BEHAVIOUR_IF_STAGE2_FAILS=2 \
    TERM=xterm

# s6 overlay
RUN apk --update add wget curl unzip socat \
 && wget -O /tmp/s6-overlay.tar.gz  "https://github.com/just-containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-amd64.tar.gz" \
 && tar xvfz /tmp/s6-overlay.tar.gz -C / \
 && rm -f /tmp/s6-overlay.tar.gz \
 && curl -o /tmp/consul_template.zip --insecure https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \
 #&& curl -o /tmp/consul_template.zip --insecure https://circle-artifacts.com/gh/duggan/build-consul-template/29/artifacts/0/tmp/circle-artifacts.BzH9kiA/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \
 && unzip /tmp/consul_template.zip \
 && mv consul-template /usr/bin  \
 && rm -rf /tmp/* \
 && apk del wget unzip

# root filesystem
COPY rootfs /

EXPOSE 80 1936

ENTRYPOINT ["/init"]
