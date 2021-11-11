FROM tomcat:latest
MAINTAINER Nick Hilhorst <nick.hilhorst@kpnmail.nl>
# Based on wadahiro/docker-openam-nightly and wstrange/openam-base-nightly

# TODO: send all tomcat/catalina logging to stdout or stderr by configuring
# java.util.logging.ConsoleHandler with a JSON based fomatter like
# https://github.com/SYNAXON/logstash-util-formatter, probably by replacing
# /usr/local/tomcat/conf/logging.properties

# Tomcat options as recommended on http://openam.forgerock.org/doc/bootstrap/getting-started/index.html
ENV CATALINA_OPTS="$CATALINA_OPTS -Xmx1024m -XX:MaxPermSize=256m"

# Download the WAR file for the OpenAM nightly build
# Trick taken from wadahiro/docker-openam-nightly!
RUN curl http://download.forgerock.org/downloads/openam/openam_link.js | \
	grep -o "http://.*\.war" | \
	xargs curl -o webapps/openam.war

# Add ~/openam/ and ~/.openamcfg/ as volumes, which makes the configuration
# persistent
VOLUME /root/openam /root/.openamcfg
