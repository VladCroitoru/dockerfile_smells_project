FROM beresfordt/alpine-java8

MAINTAINER Tom Beresford

# Create dirs
RUN mkdir -p /opt/liquibase &&\
  mkdir -p /opt/jdbc_drivers &&\
  mkdir -p /home/duser &&\
  mkdir /scripts

# Add volume
VOLUME ["/changelogs"]

# Add user
RUN addgroup -S -g 433 duser && \
  adduser -u 431 -S -G duser -H -s /sbin/nologin duser && \
  chown -R duser:duser /home/duser

# Add liquibase
ADD http://repo1.maven.org/maven2/org/liquibase/liquibase-core/3.3.0/liquibase-core-3.3.0-bin.tar.gz /opt/liquibase/liquibase-core-3.3.0-bin.tar.gz
WORKDIR /opt/liquibase
RUN tar -xzf liquibase-core-3.3.0-bin.tar.gz &&\
  rm liquibase-core-3.3.0-bin.tar.gz &&\
  chmod +x /opt/liquibase/liquibase &&\
  ln -s /opt/liquibase/liquibase /usr/local/bin/

WORKDIR /

# Add postgres driver
ADD http://central.maven.org/maven2/org/postgresql/postgresql/9.3-1102-jdbc41/postgresql-9.3-1102-jdbc41.jar /opt/jdbc_drivers/postgresql-9.3-1102-jdbc41.jar
RUN chmod 644 /opt/jdbc_drivers/postgresql-9.3-1102-jdbc41.jar

# Add update script
COPY update.sh /scripts/
RUN chmod +x /scripts/update.sh

# Prepare for running container
WORKDIR /home/duser
USER duser
CMD ["/scripts/update.sh"]
