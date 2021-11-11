FROM        alpine
MAINTAINER  deathowl <deathowlzz@gmail.com>
RUN apk add --update curl bash ca-certificates openssl && update-ca-certificates 
RUN wget https://releases.hashicorp.com/consul-template/0.16.0/consul-template_0.16.0_linux_amd64.zip -O /tmp/consul-template_0.16.0_linux_amd64.zip
RUN unzip /tmp/consul-template_0.16.0_linux_amd64.zip -d /usr/local/bin
RUN wget https://releases.hashicorp.com/consul/0.7.1/consul_0.7.1_linux_amd64.zip -O /tmp/consul_0.7.1_linux_amd64.zip
RUN unzip /tmp/consul_0.7.1_linux_amd64.zip -d /usr/local/bin
RUN wget https://github.com/prometheus/prometheus/releases/download/v1.3.1/prometheus-1.3.1.linux-amd64.tar.gz -O /tmp/prom.tar.gz
RUN tar -xzC /tmp/ -f /tmp/prom.tar.gz
RUN mv /tmp/prometheus-1.3.1.linux-amd64/prometheus /usr/local/bin/prometheus
RUN mv /tmp/prometheus-1.3.1.linux-amd64/promtool  /usr/local/bin/promtool
RUN mkdir /etc/prometheus
RUN mv /tmp/prometheus-1.3.1.linux-amd64/prometheus.yml /etc/prometheus/prometheus.yml
RUN mkdir /usr/share/prometheus
RUN mv /tmp/prometheus-1.3.1.linux-amd64/console_libraries /usr/share/prometheus
RUN mv /tmp/prometheus-1.3.1.linux-amd64/consoles /usr/share/prometheus
RUN rm -rf /tmp/*
RUN rm -rf /var/cache/apk/*
ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT /entrypoint.sh
EXPOSE     9090

