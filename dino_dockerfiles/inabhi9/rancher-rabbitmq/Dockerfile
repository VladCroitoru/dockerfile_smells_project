FROM rabbitmq:3.6-management

RUN apt-get update && apt-get install -y supervisor
ADD https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-amd64 /usr/bin/confd

RUN chmod +x /usr/bin/confd
ADD ./conf.d /etc/confd/conf.d
ADD ./templates /etc/confd/templates

ENV CONFD_ARGS=
COPY programs.conf /etc/supervisor/conf.d/programs.conf
COPY docker-xentrypoint.sh /
RUN chmod +x /docker-xentrypoint.sh

VOLUME /data/confd
VOLUME /opt/rancher/bin
VOLUME /etc/rabbitmq

ENTRYPOINT ["/docker-xentrypoint.sh", "docker-entrypoint.sh"]
CMD ["supervisord", "-n"]

