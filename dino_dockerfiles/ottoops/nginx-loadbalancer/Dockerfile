FROM nginx:1.9.2
MAINTAINER Paul Otto <paul@ottoops.com>

ENV CONSUL_TEMPLATE_VERSION=0.10.0

RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update -qq && \
    apt-get -y install curl runit && \
    rm -rf /var/lib/apt/lists/*

RUN curl -L https://github.com/hashicorp/consul-template/releases/download/v${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.tar.gz | tar -C /usr/local/bin --strip-components 1 -zxf -

ADD nginx.service /etc/service/nginx/run
ADD consul-template.service /etc/service/consul-template/run

RUN rm -v /etc/nginx/nginx.conf
ADD nginx.conf /etc/nginx/nginx.conf

RUN rm -v /etc/nginx/conf.d/*
ADD services.tmpl /etc/consul-templates/services.tmpl

CMD ["/usr/bin/runsvdir", "/etc/service"]
