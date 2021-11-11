FROM jboss/wildfly:10.1.0.Final

# Default values - overridable at runtime when creating a container
ENV WF_ADMIN_USERNAME=wildfly-ci \
    WF_ADMIN_PASSWORD=wildfly-ci \
    WF_BIND=0.0.0.0 \
    WF_MGMT_BIND=0.0.0.0 \
    WF_CONFIG=standalone.xml \
    WF_ARGS=''

# Switch back to root to handle initialization
USER root

# Use gosu (https://github.com/tianon/gosu) to start WildFly as jboss user at the end of entrypoint script
RUN set -ex \
    && yum install wget -y \
    && curl --version \
	&& wget -O /usr/bin/gosu "https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64" \
	&& wget -O  /tmp/gosu.asc "https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64.asc" \
	&& export GNUPGHOME="$(mktemp -d)" \
	&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
	&& gpg --batch --verify /tmp/gosu.asc /usr/bin/gosu \
	&& rm -r "$GNUPGHOME" /tmp/gosu.asc \
	&& chmod +x /usr/bin/gosu \
	&& gosu nobody true

COPY docker-entrypoint.sh /docker-entrypoint.sh

VOLUME /opt/jboss/wildfly/standalone/data /opt/jboss/wildfly/standalone/log

EXPOSE 9990

CMD ["/docker-entrypoint.sh"]
