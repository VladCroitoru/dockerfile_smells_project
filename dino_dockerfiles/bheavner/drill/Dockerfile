# based on the sequenceiq/drill dockerfile at
# https://hub.docker.com/r/sequenceiq/drill/~/dockerfile/

# start with the OpenJDK version 8 image
FROM openjdk:8
MAINTAINER bheavner

# get drill version 1.10.0
RUN wget http://apache.mirrors.hoobly.com/drill/drill-1.10.0/apache-drill-1.10.0.tar.gz

# create drill folder
RUN mkdir -p /opt/drill

# extract Drill
RUN tar -xvzf apache-drill-1.10.0.tar.gz -C /opt/drill

# add bootstrap.sh
RUN /bin/printf %"s\n" \
  '#!/bin/bash' \
  ': ${DRILL_HOME:=/opt/drill/apache-drill-1.10.0}' \
  'cd /opt/drill/apache-drill-1.10.0;' \
  'bin/sqlline -u jdbc:drill:zk=local' > \
  /etc/bootstrap.sh
RUN chown root:root /etc/bootstrap.sh
RUN chmod 700 /etc/bootstrap.sh
ENV BOOTSTRAP /etc/bootstrap.sh
