FROM haproxy:1.6.9-alpine

ENV CT_VERSION 0.15.0
ENV CONSUL_SERVICE_NAME_REGEX .*
ENV HAPROXY_MAXCONN 1024
ENV HAPROXY_MODE tcp
ENV HAPROXY_BALANCE roundrobin
ENV HAPROXY_CONNECT_TIMEOUT 5s
ENV HAPROXY_SERVER_TIMEOUT 60s
ENV HAPROXY_CLIENT_TIMEOUT 60s
ENV HAPROXY_CHECK_TIMEOUT 5s
ENV HAPROXY_CHECK_INTER 2s
ENV HAPROXY_CHECK_RISE 2
ENV HAPROXY_CHECK_FALL 2
ENV HAPROXY_OPTIONS option redispatch,option tcp-check

RUN apk --no-cache add --update unzip

ADD https://releases.hashicorp.com/consul-template/${CT_VERSION}/consul-template_${CT_VERSION}_linux_amd64.zip consul_template_latest_linux_amd64.zip
RUN unzip consul_template_latest_linux_amd64.zip && rm -f consul_template_latest_linux_amd64.zip
RUN mv consul-template /usr/bin/
RUN chmod 555 /usr/bin/consul-template

# Configure consul-template
RUN mkdir -p /etc/consul-template
VOLUME /etc/consul-template
ADD consul-template.cfg /etc/consul-template/consul-template.cfg
ADD haproxy.tmpl /etc/consul-template/haproxy.tmpl

# Create volume for HAProxy config. Only really useful for monitoring/debugging.
RUN mkdir -p /etc/haproxy
VOLUME /etc/haproxy

ENTRYPOINT ["/usr/bin/consul-template", "-config", "/etc/consul-template/consul-template.cfg"]
