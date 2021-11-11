FROM gennyproject/wildfly:v7.0.0 
RUN apk update && apk add git 

USER root

ADD docker-entrypoint.sh /opt/jboss/docker-entrypoint.sh
ADD docker-entrypoint2.sh /opt/jboss/

EXPOSE 8080
#RUN mkdir /opt/realm
#RUN mkdir /opt/jboss/wildfly/realm
#RUN mkdir /realm

ENTRYPOINT [ "/opt/jboss/docker-entrypoint2.sh" ]
#ADD realm /opt/realm
ADD qwanda-service-ear/target/qwanda-service-ear.ear $JBOSS_HOME/standalone/deployments/qwanda-service-ear.ear
