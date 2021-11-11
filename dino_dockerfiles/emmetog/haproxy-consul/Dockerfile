FROM ubuntu:xenial

MAINTAINER Emmet O'Grady <emmet789@gmail.com>

ENV CONSUL_TEMPLATE_VERSION 0.14.0

RUN apt-get update \
    && apt-get install -y \
        haproxy \
        curl \
        unzip \
    && curl -L -o /tmp/consul-template.zip https://releases.hashicorp.com/consul-template/0.14.0/consul-template_0.14.0_linux_amd64.zip \
    && cd /tmp \
    && unzip consul-template.zip \
    && cp /tmp/consul-template /usr/local/bin/consul-template \
    && rm -rf /tmp/consul* \
    && chmod a+x /usr/local/bin/consul-template \
    && apt-get remove -y curl unzip \
    && apt-get autoremove -y \
    && apt-get autoclean

ENTRYPOINT ["/bin/sh"]
CMD ["/start.sh"]

ADD haproxy.conf /etc/haproxy/haproxy.cfg

ADD start.sh /start.sh
RUN chmod u+x /start.sh
ADD reload_haproxy.sh /reload_haproxy.sh
RUN chmod u+x /reload_haproxy.sh