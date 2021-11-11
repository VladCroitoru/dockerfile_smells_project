FROM sdempsay/docker-felix-developer
MAINTAINER Shawn Dempsay <shawn@dempsay.org>

#
# Add in osgi-jaxrs stuff
#
ADD http://repo1.maven.org/maven2/com/eclipsesource/osgi-jaxrs-connector/3.2.1/osgi-jaxrs-connector-3.2.1.jar /opt/felix/current/bundle/
ADD http://repo1.maven.org/maven2/com/eclipsesource/jaxrs/jersey-all/2.10.1/jersey-all-2.10.1.jar /opt/felix/current/bundle/

#
# We use jackson stuff too
#
ADD http://repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-core/2.4.0/jackson-core-2.4.0.jar /opt/felix/current/bundle/
ADD http://repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-annotations/2.4.0/jackson-annotations-2.4.0.jar /opt/felix/current/bundle/
ADD http://repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-databind/2.4.0/jackson-databind-2.4.0.jar /opt/felix/current/bundle/

## Inherited from the parent, here for reference
# EXPOSE 8080
# VOLUME /opt/felix/current/load
# CMD cd /opt/felix/current && java -jar bin/felix.jar
