FROM tomcat:6
ENV DEBIAN_FRONTEND noninteractive

RUN rm -rf $CATALINA_HOME/webapps/ROOT
COPY webapps/MapAnalyst $CATALINA_HOME/webapps/ROOT
