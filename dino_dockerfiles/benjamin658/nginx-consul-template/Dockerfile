FROM nginx:stable

MAINTAINER benjamin658gae@gmail.com

RUN apt-get update -qq && apt-get -y install curl unzip

ENV CONSUL_TEMPLATE_VERSION 0.18.5
ENV CONSUL_SERVER consul:8500

ADD https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS /tmp/
ADD https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip /tmp/
ADD ./entry.sh /entry.sh

RUN cd /tmp && \ 
    sha256sum -c consul-template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS 2>&1 | grep OK && \
    unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \ 
    mv consul-template /bin/consul-template && \
    rm -rf /tmp

RUN mkdir /etc/consul-templates
ADD nginx.ctmpl /etc/consul-templates
ADD gzip.conf /etc/nginx/conf.d

CMD ["/entry.sh"]
