FROM khirin/alpine

ARG     UID="2000"
ARG     GID="2000"
ARG     PORT="3306"

LABEL 	maintainer="khirin" \
	name="MariaDB" \
        mariadb_version="10.1.22" \
	date="20170315" \
        image_version="1.2" \
	user="mysql" \
	uid=${UID} \
	group="mysql" \
	gid=${GID}

ENV	DATABASE="mariadb" \
	DB_USER="mariadb" \
	DB_USER_PASSWORD="dXNlcnBhc3N3b3JkCg==" \
	DB_ROOT_PASSWORD="cm9vdHBhc3N3b3JkCg==" \
	CLIENT_HOST="web.mariadbnetwork"

COPY ["sources/init.sh", "/tmp/init.sh"]

RUN	addgroup -g ${GID} mysql \
	&& adduser -D -G mysql -g "MySQL User" -s /bin/sh -u ${UID} mysql \
	&& apk --update add mariadb mariadb-client \
	&& rm -rf /var/cache/apk/* \
	&& /tmp/init.sh

VOLUME ["/conf", "/scripts", "/var/lib/mysql"]

EXPOSE ${PORT}

USER mysql

ENTRYPOINT ["/scripts/start.sh"]
