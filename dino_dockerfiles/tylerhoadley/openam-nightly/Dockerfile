FROM tomcat:8-jre8

MAINTAINER tyler.hoadley[AT]computersthatwork[DOT]ca

# Run bash shell in order to run apt-get commands
RUN /bin/bash
# install jdk for jar
RUN apt-get update && apt-get install -y wget openjdk-8-jdk --no-install-recommends \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /tmp/openam_exploded
RUN mkdir -p /opt/openam/config
WORKDIR /tmp/openam_exploded


# download openam nightly build war
# Trick taken from wadahiro/docker-openam-nightly!
RUN curl http://download.forgerock.org/downloads/openam/openam_link.js | \
   grep -o "http://.*\.war" | xargs curl -o /tmp/openam_exploded/openam-org.war

RUN jar xvf /tmp/openam_exploded/openam-org.war
RUN echo "configuration.dir=/opt/openam/config" >> WEB-INF/classes/bootstrap.properties
RUN rm -rf /tmp/openam_exploded/openam-org.war
RUN jar cvf /usr/local/tomcat/webapps/openam.war ./*

RUN apt-get remove --purge openjdk-8-jdk -y && apt-get -y autoremove  && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV CATALINA_HOME=/usr/local/tomcat
ENV PATH=$CATALINA_HOME/bin:$PATH
WORKDIR $CATALINA_HOME

EXPOSE 8080

ADD run-openam.sh /tmp/run-openam.sh
RUN chmod 777 /tmp/run-openam.sh

CMD ["/tmp/run-openam.sh"]
