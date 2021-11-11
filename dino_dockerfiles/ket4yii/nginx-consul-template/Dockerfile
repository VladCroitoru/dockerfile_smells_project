FROM nginx:alpine
MAINTAINER Alexey Boyko <ket4yiit@gmail.com>

ENV CONSUL_TEMPLATE_VER 0.16.0
ENV CONSUL_SERVER localhost:8500
ENV NGINX_CONF_PATH /etc/nginx/conf.d/generated.conf
ENV NGINX_TMPL_PATH /tmp/nginx.ctmpl

ADD https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VER}/consul-template_${CONSUL_TEMPLATE_VER}_linux_amd64.zip /tmp/consul-template.zip

RUN unzip /tmp/consul-template.zip -d /usr/bin && \
    chmod +x /usr/bin/consul-template && \
    rm /tmp/consul-template.zip

COPY entrypoint.sh /entrypoint.sh

CMD "/entrypoint.sh"
