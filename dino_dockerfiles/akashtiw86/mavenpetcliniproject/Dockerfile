FROM java:8-jre

ENV CATALINA_HOME /usr/local/tomcat
ENV PATH $CATALINA_HOME/bin:$PATH

RUN mkdir -p "$CATALINA_HOME" \
    && apt-get update

WORKDIR $CATALINA_HOME

ENV TOMCAT_MAJOR 8
ENV TOMCAT_VERSION 8.5.30
ENV TOMCAT_TGZ_URL https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/
RUN set -x \
    && wget $TOMCAT_TGZ_URL/apache-tomcat-$TOMCAT_VERSION.tar.gz \
    && tar -xvf apache-tomcat-8.5.30.tar.gz --strip-components=1

ADD ./petclinic.war $CATALINA_HOME/webapps/

EXPOSE 8080
CMD ["catalina.sh", "run"]
