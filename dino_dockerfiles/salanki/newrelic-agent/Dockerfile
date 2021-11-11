FROM progrium/busybox
MAINTAINER support@tutum.co

ENV NEW_RELIC_LICENSE_KEY **CHANGE_ME**
ENV VERSION 2.3.0.129

ADD https://download.newrelic.com/server_monitor/release/newrelic-sysmond-$VERSION-linux.tar.gz /tmp/
RUN gunzip -c /tmp/newrelic-sysmond-$VERSION-linux.tar.gz | tar xf - -C /tmp && \
	mv /tmp/newrelic-sysmond-$VERSION-linux /newrelic && \
	mkdir -p /etc/newrelic && \
	mv /newrelic/nrsysmond.cfg /etc/newrelic/nrsysmond.cfg
ADD run.sh /
CMD ["/run.sh"]

# Output of: yaml2json tutum.yml | tr "\n" " " | sed 's/"/\\"/g'
LABEL co.tutum.yml="{   \"newrelic\": {     \"image\": \"tutum/newrelic-agent\",     \"restart\": \"on-failure\",     \"privileged\": true,     \"volumes\": [       \"/var/run/docker.sock:/var/run/docker.sock\",       \"/dev:/dev\",       \"/sys:/sys\"     ],     \"environment\": [       \"NEW_RELIC_LICENSE_KEY=<LICENSE>\",       \"HOSTNAME=$TUTUM_NODE_HOSTNAME\"     ],     \"deployment_strategy\": \"every_node\"   } }"
