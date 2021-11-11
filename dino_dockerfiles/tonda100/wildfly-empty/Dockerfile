FROM jboss/wildfly:10.1.0.Final
MAINTAINER Antonin Stoklasek
ENV WILDFLY_HOME /opt/jboss/wildfly
ENV DEPLOY_DIR ${WILDFLY_HOME}/standalone/deployments/

# setup timezone
ENV TZ=Europe/Prague
USER root
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
USER jboss

COPY standalone.conf $WILDFLY_HOME/bin/
# necessary to create a folder before start, otherwise the gc.log and heapdump will not be created
RUN mkdir /opt/jboss/wildfly/standalone/log/

ENTRYPOINT ${WILDFLY_HOME}/bin/standalone.sh -b=0.0.0.0
EXPOSE 8080