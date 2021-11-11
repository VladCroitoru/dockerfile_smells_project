FROM tomcat:7.0.91-jre8-alpine
# see also pom.xml in java project

MAINTAINER Dirk Steinkopf "https://github.com/dsteinkopf"

ENV BRANCH_NAME=master
ENV DOWNLOAD_URL=https://tuerauf.dirkness.de/tuerauf-backend-java/tuerauf-$BRANCH_NAME.war

COPY setenv.sh $CATALINA_HOME/bin/

VOLUME $CATALINA_HOME/conf

RUN set -x \
    && wget -q --output-document "${CATALINA_HOME}/webapps/tuerauf.war" "$DOWNLOAD_URL" \
    && touch                  "${CATALINA_HOME}/webapps/tuerauf.war" \
    && chmod -R 700           "${CATALINA_HOME}/conf" \
    && chmod -R 700           "${CATALINA_HOME}/temp" \
    && chmod -R 700           "${CATALINA_HOME}/logs" \
    && chmod -R 700           "${CATALINA_HOME}/work" \
    && chmod -R 700           "${CATALINA_HOME}/webapps" \
    && chown -R daemon:daemon "${CATALINA_HOME}/conf" \
    && chown -R daemon:daemon "${CATALINA_HOME}/temp" \
    && chown -R daemon:daemon "${CATALINA_HOME}/logs" \
    && chown -R daemon:daemon "${CATALINA_HOME}/work" \
    && chown -R daemon:daemon "${CATALINA_HOME}/webapps"

#see tomcat: EXPOSE 8080
#see tomcat: WORKDIR $CATALINA_HOME

USER daemon:daemon

CMD ["catalina.sh", "run"]
