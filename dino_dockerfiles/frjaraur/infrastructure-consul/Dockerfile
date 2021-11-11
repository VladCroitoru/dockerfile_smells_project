FROM alpine

RUN apk --update add curl unzip supervisor

WORKDIR /apps

RUN curl -s -o consul.zip https://releases.hashicorp.com/consul/0.6.4/consul_0.6.4_linux_amd64.zip && unzip consul.zip && \
curl -sL https://github.com/sequenceiq/docker-alpine-dig/releases/download/v9.10.2/dig.tgz|tar -xzv -C /usr/local/bin/


COPY entrypoint.sh /entrypoint.sh

EXPOSE 8300
EXPOSE 8301 8301/udp 8302 8302/udp
EXPOSE 8400 8500 8600 8600/udp

VOLUME /data

CMD ["start"]

ENTRYPOINT ["/entrypoint.sh"]

# COPY config /config
#
# COPY  supervisor /etc/supervisor/conf.d/
#
#
# COPY entrypoint.sh /entrypoint.sh
#
# ENV COLLECTD_SERVER_NAME "collectdserver"
#
# ENV COLLECTD_SERVER_PORT 9090
#
# ENV CONSUL_SERVER_NAME "consulserver"
#
# ENV CONSUL_SERVER_PORT 9091
#
# ENTRYPOINT ["/entrypoint.sh"]
#
#CMD ["start"]
