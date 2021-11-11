FROM alpine:3.2

MAINTAINER Arlindo Santos <sarlindo@hotmail.com>


ENV CONSUL_TEMPLATE_VERSION=0.11.1

RUN apk add --update bash 
RUN apk add --update haproxy=1.5.14-r0 
RUN apk add --update ca-certificates

ADD https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip /

RUN unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \ 
    mv consul-template /usr/local/bin/consul-template && \ 
    rm -rf /consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \ 
    rm -rf consul-template

RUN mkdir -p /haproxy /consul-template/config.d /consul-template/template.d

ADD config/ /consul-template/config.d/
ADD template/ /consul-template/template.d/
ADD launch.sh /launch.sh

CMD ["/launch.sh"]
