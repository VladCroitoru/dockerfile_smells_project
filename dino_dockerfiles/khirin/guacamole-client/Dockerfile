FROM khirin/tomcat

LABEL 	maintainer="khirin" \
	name="Guacamole Client Image" \
        guacamole_version="0.9.12" \
	date="20170508" \
        image_version="1.2"

ARG     GUACAMOLE_HOME="/guacamole"
ARG     GUACAMOLE_DB_SRV="guacamole-db"
ARG     GUACAMOLE_DB_PORT="3306"
ARG     GUACAMOLE_DB="guacamole"
ARG     GUACAMOLE_DB_USER="guacamole"
ARG     GUACAMOLE_DB_PASSWORD="Z3VhY2Ftb2xlCg=="
ARG     GUACAMOLE_GUACD_SRV="guacamole-server"
ARG     GUACAMOLE_GUACD_PORT="4822"

ENV     MAX_MEM="640"
ENV     JAVA_OPTS="-Xmx${MAX_MEM}m" \
	MYSQL_CONNECTOR_VERSION="5.1.42" \
	GUACAMOLE_VERSION="0.9.12" \
	GUACAMOLE_HOME="${GUACAMOLE_HOME}" \
	GUACAMOLE_DB_SRV="${GUACAMOLE_DB_SRV}" \
	GUACAMOLE_DB_PORT="${GUACAMOLE_DB_PORT}" \
	GUACAMOLE_DB="${GUACAMOLE_DB}" \
	GUACAMOLE_DB_USER="${GUACAMOLE_DB_USER}" \
	GUACAMOLE_DB_PASSWORD="${GUACAMOLE_DB_PASSWORD}" \
	GUACAMOLE_GUACD_SRV="${GUACAMOLE_GUACD_SRV}" \
	GUACAMOLE_GUACD_PORT="${GUACAMOLE_GUACD_PORT}"

COPY ["sources/guacamole-${GUACAMOLE_VERSION}-incubating.war", "sources/guacamole-auth-jdbc-${GUACAMOLE_VERSION}-incubating.tar.gz", "sources/mysql-connector-java-${MYSQL_CONNECTOR_VERSION}.tar.gz", "sources/init.sh", "/tmp/"]

USER root

RUN	mv /tmp/guacamole-*-incubating.war ${CATALINA_HOME}/webapps/guacamole.war \
	&& /tmp/init.sh

USER tomcat
