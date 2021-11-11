FROM fabric8/base-sti

MAINTAINER Dhiraj Bokde <dhirajsb@gmail.com>
LABEL io.k8s.description="Platform for building and running Karaf4 based applications" \
            io.k8s.display-name="Karaf4" \
# users will expose using oc commands
#            io.openshift.expose-services="8080:http" \
            io.openshift.s2i.scripts-url=https://raw.githubusercontent.com/dhirajsb/karaf4-sti/master/.sti/bin/ \
# deprecated script url for backward compatibility
            io.s2i.scripts-url=https://raw.githubusercontent.com/dhirajsb/karaf4-sti/master/.sti/bin/ \
            io.openshift.s2i.destination=/tmp \
            io.openshift.tags="builder,karaf4"

USER root

# download jolokia in the sti builder
RUN mkdir /opt/jolokia && curl -L http://central.maven.org/maven2/org/jolokia/jolokia-jvm/1.3.1/jolokia-jvm-1.3.1-agent.jar > /opt/jolokia/jolokia.jar

USER jboss

CMD ["/usr/bin/usage"]
