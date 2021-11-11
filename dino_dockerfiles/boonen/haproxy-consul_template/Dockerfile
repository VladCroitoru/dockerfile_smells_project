FROM haproxy:1.6.5-alpine
MAINTAINER Jan Boonen <jan.boonen@geodan.nl>

ENV CONSUL_TEMPLATE_HOME /opt/consul
ENV CONSUL_TEMPLATE_VERSION 0.15.0
ENV CONSUL_TEMPLATE_MD5 b7561158d2074c3c68ff62ae6fc1eafe8db250894043382fb31f0c78150c513a
ENV CONSUL_ADDRESS 127.0.0.1:8500

RUN apk-add --update unzip &&
  curl -SL "https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" -o consul_template.zip \
  && echo "${CONSUL_TEMPLATE_MD5} consul_template.zip" | md5sum -c \
  && mkdir -p ${CONSUL_TEMPLATE_HOME} \
  && tar -xzf consul_template.zip -C ${CONSUL_TEMPLATE_HOME} \
  && rm consul_template.zip \
  && rm -rf /var/cache/apk/*

CMD ["sh", "-c", "'consul-template -consul ${CONSUL_ADDRESS} -template "/usr/local/etc/haproxy/haproxy.cfg.ctmpl:/usr/local/etc/haproxy/haproxy.cfg" -retry 30s' && haproxy -f /usr/local/etc/haproxy/haproxy.cfg"]