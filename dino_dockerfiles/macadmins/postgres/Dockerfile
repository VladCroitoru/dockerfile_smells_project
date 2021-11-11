# Version 0.0.2

FROM postgres

MAINTAINER Nick McSpadden <nmcspadden@gmail.com>

ENV DB_NAME database
ENV DB_USER admin
ENV DB_PASS password

ADD setupRemoteConnections.sh /docker-entrypoint-initdb.d/setupRemoteConnections.sh
RUN chmod 755 /docker-entrypoint-initdb.d/setupRemoteConnections.sh
ADD setup-database.sh /docker-entrypoint-initdb.d/
RUN chmod 755 /docker-entrypoint-initdb.d/setup-database.sh
