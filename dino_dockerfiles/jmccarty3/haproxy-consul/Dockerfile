FROM gliderlabs/alpine

MAINTAINER Steven Borrelli <steve@aster.is>

ENV CONSUL_TEMPLATE_VERSION=0.14.0

RUN apk-install bash haproxy ca-certificates

ADD https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip /

RUN unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \
    mv consul-template /usr/local/bin/consul-template && \
    rm -rf /consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \
    rm -rf /consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64

RUN mkdir -p /haproxy /consul-template/config.d /consul-template/template.d /etc/rsyslog.d

ADD config/ /consul-template/config.d/
ADD template/ /consul-template/template.d/
ADD launch.sh /launch.sh
ADD haproxy.conf /etc/rsyslog.d/

CMD ["/launch.sh"]
