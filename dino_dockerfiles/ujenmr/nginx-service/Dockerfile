FROM nginx

LABEL maintainer "Ievgen Khmelenko <ujenmr@gmail.com>"

ENV SERVICE_NAME "nginx-service"
ENV SERVICE_CHECK_TCP "true"
ENV SERVICE_CHECK_INTERVAL "15s"
ENV SERVICE_TAGS "master,system"

ENV CONSUL_TEMPLATE_VERSION=0.18.1

RUN apt-get update && \
    apt-get install -y --no-install-recommends unzip curl && \
    curl https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip > /var/tmp/consul-template.zip && \
    unzip /var/tmp/consul-template.zip -d /usr/bin/ && \
    apt-get purge -y curl unzip && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/nginx/*

ADD nginx /etc/nginx
ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

CMD ["/docker-entrypoint.sh"]
