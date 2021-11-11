FROM antonmry/restcomm-sip-servlets-jboss-docker:3.1.633

MAINTAINER Antón R. Yuste

USER jboss

ADD config/docker/hellosipworld-1.0-SNAPSHOT.war $JBOSS_HOME/standalone/deployments/
ADD config/dar/mobicents-dar.properties $JBOSS_HOME/standalone/configuration/dars/

# Only for test
#RUN $JBOSS_HOME/bin/add-user.sh admin Admin#70365 --silent
