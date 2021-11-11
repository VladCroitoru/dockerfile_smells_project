FROM dockerfile/java

MAINTAINER Alessandro Arnone <arnone.alessandro@gmail.com>

RUN mkdir -p /opt/flyway && mkdir -p /locations

RUN curl -L http://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/3.2.1/flyway-commandline-3.2.1.tar.gz -o /tmp/flyway.tar.gz

RUN tar -xzf /tmp/flyway.tar.gz --strip 1 -C /opt/flyway \
	&& rm -rf /tmp/flyway.tar.gz


ADD run-flyway.sh /opt/

RUN chmod +x /opt/run-flyway.sh

ENTRYPOINT ["/opt/run-flyway.sh"]

