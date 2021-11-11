FROM debian:jessie
MAINTAINER David Hong <david.hong@peopleplan.com.au>

ENV DEBIAN_FRONTEND=noninteractive \
	LIQUIBASE_VERSION=3.4.2

# install wget, java and mysql driver
RUN apt-get update \
	&& apt-get install -yq --no-install-recommends \
		wget \
		netcat \
		default-jre \
		libmysql-java \
	&& apt-get clean \
	&& rm -r /var/lib/apt/lists/*

RUN wget -q --no-check-certificate https://github.com/liquibase/liquibase/releases/download/liquibase-parent-${LIQUIBASE_VERSION}/liquibase-${LIQUIBASE_VERSION}-bin.tar.gz -O /tmp/liquibase-${LIQUIBASE_VERSION}-bin.tar.gz \
	&& mkdir -p /opt/liquibase \
	&& tar -xf /tmp/liquibase-${LIQUIBASE_VERSION}-bin.tar.gz -C /opt/liquibase \
	&& chmod +x /opt/liquibase/liquibase \
	&& ln -s /opt/liquibase/liquibase /usr/local/bin/

VOLUME /changelogs
WORKDIR /changelogs

COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["update"]
