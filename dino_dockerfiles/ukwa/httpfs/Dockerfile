FROM maven:3-jdk-7 AS build-env

COPY pom.xml /usr/src/httpfs/pom.xml
COPY src /usr/src/httpfs/src

WORKDIR /usr/src/httpfs

RUN mvn package -Pdist


FROM openjdk:8-jre

COPY --from=build-env /usr/src/httpfs/target/hadoop-hdfs-httpfs-0.20.2-cdh3u7-SNAPSHOT.tar.gz /hadoop-hdfs-httpfs.tar.gz

RUN cd /opt && \
  tar xvfz /hadoop-hdfs-httpfs.tar.gz && \
  ln -s hadoop-hdfs-httpfs-* hadoop-hdfs-httpfs

WORKDIR /opt/hadoop-hdfs-httpfs

# Add a httpfs group with two users
RUN groupadd -r httpfs && useradd --no-log-init -r -g httpfs access && useradd --no-log-init -r -g httpfs ingest && useradd --no-log-init -r -g httpfs tomcat

# Allow either to run the service
RUN chgrp -R httpfs /opt && chmod g+rwx -R /opt

# Default to running as the access user
USER access

CMD ./sbin/httpfs.sh run

