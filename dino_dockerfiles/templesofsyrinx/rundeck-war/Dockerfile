# The current version of RunDeck requires Java 7 JRE
FROM tomcat:7-jre7

# Current version of RunDeck (target)
ENV RUNDECK_VERSION 2.5.3
ENV RUNDECK_DOWNLOAD_URL http://download.rundeck.org
ENV RUNDECK_WAR_URL $RUNDECK_DOWNLOAD_URL/war/rundeck-$RUNDECK_VERSION.war
ENV APP_CONTEXT rundeck

WORKDIR $CATALINA_HOME/webapps/$APP_CONTEXT

RUN set -x \
	&& curl -fSL "$RUNDECK_WAR_URL" -o rundeck.war \
	&& curl -fSL "$RUNDECK_WAR_URL.asc" -o rundeck.war.asc \
	&& unzip rundeck.war \
	&& rm rundeck.war*

# https://github.com/rundeck/rundeck/issues/1187
# the normal jetty/launcher installer creates a "log4j.properties" file for you.
# You would need to create one within the classpath for the webapp, e.g. at $CATALINA_HOME/webapps/rundeck/WEB-INF/classes/log4j.properties
RUN touch WEB-INF/classes/log4j.properties

ADD ./run.sh /
RUN chmod +x /run.sh

CMD ["/run.sh", "catalina.sh", "run"]
