FROM nginx:1.17
MAINTAINER DJ Enriquez

RUN apt-get update && \
apt-get -y install curl runit cron logrotate unzip && \
rm -rf /var/lib/apt/lists/* && \
mkdir /etc/nginx/tcp-proxy/ && \
rm -v /etc/nginx/conf.d/* 

# Install Consul-Template
ENV CT_VERSION 0.22.0
ENV CT_FILE consul-template_${CT_VERSION}_linux_amd64.zip
ENV CT_URL https://releases.hashicorp.com/consul-template/${CT_VERSION}/$CT_FILE
RUN curl -O $CT_URL && \
unzip $CT_FILE -d /usr/local/bin && \
rm -rf $CT_FILE

# RUNIT services
ADD src/services/nginx.service /etc/service/nginx/run
ADD src/services/consul-template.service /etc/service/consul-template/run
ADD src/services/cron.service /etc/service/cron/run

# Add consul-template files
ADD /src/consul-templates/ /etc/consul-templates/

# Log rotate files
ADD src/logrotate/ /etc/logrotate.d/

# Add crontab
ADD src/crontab /etc/crontab

# Add nginx-check
ADD src/nginx-check /usr/sbin/nginx-check

# Start commands
ADD start.sh /usr/sbin/start.sh

ENV CONSUL_ADDRESS localhost
ENV CONSUL_PORT 8500

CMD ["/usr/sbin/start.sh"]
