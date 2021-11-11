FROM openjdk:8-jre

MAINTAINER Firespring info.dev@firespring.com

# Init ENV
ENV BISERVER_VERSION=7.1 \
    BISERVER_TAG=7.1.0.0-12 \
    PGSQL_CONNECTOR_VERSION=42.1.3

# Apply JAVA_HOME
RUN . /etc/environment
ENV PENTAHO_JAVA_HOME=$JAVA_HOME \
    PENTAHO_JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64 \
    JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64

# Install Dependences
RUN apt-get update \
  && apt-get install -y wget unzip netcat postgresql-client libapr1-dev libssl-dev libtcnative-1 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV PENTAHO_HOME=/opt/pentaho
RUN mkdir ${PENTAHO_HOME} && useradd -s /bin/bash -d ${PENTAHO_HOME} pentaho && chown pentaho:pentaho ${PENTAHO_HOME}

# Download Pentaho BI Server
RUN /usr/bin/wget https://downloads.sourceforge.net/project/pentaho/Business%20Intelligence%20Server/${BISERVER_VERSION}/pentaho-server-ce-${BISERVER_TAG}.zip -O /tmp/pentaho-server-ce-${BISERVER_TAG}.zip \
  && /usr/bin/unzip -q /tmp/pentaho-server-ce-${BISERVER_TAG}.zip -d $PENTAHO_HOME \
  && rm -f /tmp/pentaho-server-ce-${BISERVER_TAG}.zip $PENTAHO_HOME/pentaho-server/promptuser.sh \
  && sed -i -e 's/\(exec ".*"\) start/\1 run/' $PENTAHO_HOME/pentaho-server/tomcat/bin/startup.sh \
  && chmod +x $PENTAHO_HOME/pentaho-server/start-pentaho.sh

# Add a default/dummy cert for https
RUN openssl req -x509 -nodes -days 365 -subj '/CN=sbf.dev' -sha256 -newkey rsa:2048 -keyout $PENTAHO_HOME/pentaho-server/tomcat/conf/pentaho.key -out $PENTAHO_HOME/pentaho-server/tomcat/conf/pentaho.crt

# Update the postgresql connector version used
RUN rm -f $PENTAHO_HOME/pentaho-server/tomcate/lib/postgresql*.jar \
  && /usr/bin/wget https://jdbc.postgresql.org/download/postgresql-${PGSQL_CONNECTOR_VERSION}.jar -O $PENTAHO_HOME/pentaho-server/tomcat/lib/postgresql-${PGSQL_CONNECTOR_VERSION}.jar

# Put custom configs in to place
RUN rm -rf $PENTAHO_HOME/pentaho-server/tomcat/conf/Catalina/* $PENTAHO_HOME/pentaho-server/tomcat/temp/* $PENTAHO_HOME/pentaho-server/tomcat/work/* $PENTAHO_HOME/pentaho-server/tomcat/logs/*
COPY config/postgresql $PENTAHO_HOME
COPY script $PENTAHO_HOME/script

# Make sure everything is owned by the pentaho user
RUN chown -R pentaho:pentaho $PENTAHO_HOME

USER pentaho
WORKDIR $PENTAHO_HOME
EXPOSE 8080
CMD ["./script/run.sh"]
