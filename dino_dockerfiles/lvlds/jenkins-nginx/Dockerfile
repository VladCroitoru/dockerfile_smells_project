FROM openresty/openresty:1.11.2.2-xenial

RUN apt-get update && apt-get install -y runit && \
    luarocks install nginx-lua-prometheus && \
    mkdir -p /var/log/nginx/ /var/run/nginx

ENV CT_URL https://releases.hashicorp.com/consul-template/0.19.5/consul-template_0.19.5_linux_amd64.zip
RUN curl -O $CT_URL && unzip consul-template_0.19.5_linux_amd64.zip -d /usr/local/bin

ADD ./conf.d /etc/nginx/conf.d/
ADD ./openresty.service /lib/systemd/system/
RUN systemctl enable openresty
ADD ./consul/nginx.service /etc/service/nginx/run
ADD ./consul/consul-template.service /etc/service/consul-template/run
RUN chmod +x /etc/service/nginx/run
RUN chmod +x /etc/service/consul-template/run

ADD ./consul/nginx.conf /etc/consul-templates/nginx.conf
ADD ./consul/index.html /etc/consul-templates/index.html
ADD ./docker-entrypoint.sh /

ADD ./nginx.conf /usr/local/openresty/nginx/conf/nginx.conf

ENTRYPOINT ["/usr/bin/runsvdir", "/etc/service"]