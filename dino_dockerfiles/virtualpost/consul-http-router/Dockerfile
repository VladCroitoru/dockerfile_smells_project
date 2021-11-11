FROM gliderlabs/alpine

EXPOSE 80

ENV CONSUL_TEMPLATE_VERSION 0.12.2

CMD ["/usr/local/bin/consul-template", "-consul", "consul.service.consul:8500", "-template", "/templates/nginx.ctmpl:/etc/nginx/nginx.conf:/reload.sh"]

RUN apk --no-cache add nginx ca-certificates wget

RUN wget -O /tmp/consul-template.zip https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \
	unzip /tmp/consul-template.zip -d /usr/local/bin/ && \
	rm /tmp/consul-template.zip && \
	mkdir /templates

ADD nginx.ctmpl /templates/nginx.ctmpl
ADD nginx.conf  /etc/nginx/nginx.conf
ADD index.html  /var/www/index.html
ADD reload.sh   /reload.sh
RUN chmod +x /reload.sh && mkdir /run/nginx && chown -R nginx /var/lib/nginx

