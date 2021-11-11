#FROM jboss/wildfly
FROM jboss/wildfly:18.0.1.Final

ENV WILDFLY /opt/jboss/wildfly

ADD target/insecure-bank.war /opt/jboss/wildfly/standalone/deployments/

EXPOSE 8080

CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0"]
