FROM telegraf

ADD https://github.com/kelseyhightower/confd/releases/download/v0.14.0/confd-0.14.0-linux-amd64 /usr/local/bin/confd
RUN chmod a+x /usr/local/bin/confd
RUN mkdir -p /etc/confd/{conf.d,templates}

ADD entrypoint_confd.sh /
ADD telegraf.conf.tmpl /etc/confd/templates/
ADD telegraf.toml /etc/confd/conf.d/

RUN chmod a+x /entrypoint_confd.sh

ENV BLEEMEO_HOSTNAME=_docker_undef
ENTRYPOINT [ "/entrypoint_confd.sh" ]
CMD [ "telegraf", "--config-directory", "/etc/telegraf/telegraf.d" ]