FROM alpine

MAINTAINER Huy Giang <gnhuy91@gmail.com>

ENV CONSUL_TEMPLATE_VERSION=0.14.0

# Update wget to get support for SSL
RUN apk --update add haproxy wget && \
    rm -rf /var/cache/apk/*

# Download consul-template
RUN wget -q --no-check-certificate https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \
    -O /tmp/consul_template.zip && \
    unzip /tmp/consul_template.zip && \
    mv consul-template /usr/bin && \
    rm -rf /tmp/*

RUN mkdir -p /consul-template/config.d /consul-template/template.d

COPY haproxy.hcl /consul-template/config.d/haproxy.hcl
COPY haproxy.ctmpl /consul-template/template.d/haproxy.ctmpl

ENTRYPOINT ["consul-template","-config=/consul-template/config.d/haproxy.hcl"]
CMD ["-consul=127.0.0.1:8500"]
