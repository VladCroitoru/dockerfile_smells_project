FROM gliderlabs/alpine:3.1

MAINTAINER Kevin van der Vlist <kvdvlist@sogyo.nl>

RUN apk update \
  && apk add nginx wget \
  && cd / \
  && wget --no-check-certificate -O consul-template.tar.gz https://github.com/hashicorp/consul-template/releases/download/v0.9.0/consul-template_0.9.0_linux_amd64.tar.gz \
  && tar xzvf /consul-template.tar.gz \
  && mv /consul-template_*/consul-template /consul-template \
  && rm -r /consul-template_* \
  && rm /consul-template.tar.gz \
  && mkdir -p /tmp/nginx/client-body \
  && apk del wget \
  && rm -rf /var/cache/apk/* 

ADD reload.sh   /reload.sh
RUN chmod +x /reload.sh
ADD index.html  /www/index.html
ADD nginx.conf  /etc/nginx/nginx.conf
ADD nginx.ctmpl /nginx.ctmpl

EXPOSE 80

ENTRYPOINT ["/consul-template"]
CMD ["-consul", "consul.service.consul:8500", "-template", "/nginx.ctmpl:/etc/nginx/nginx.conf:/reload.sh"]
