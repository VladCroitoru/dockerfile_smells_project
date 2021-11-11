FROM docker.bintray.io/jfrog/artifactory-oss

ENV ARTIFACTORY_HOME=/var/opt/jfrog/artifactory

ADD http://central.maven.org/maven2/mysql/mysql-connector-java/5.1.35/mysql-connector-java-5.1.35.jar /opt/jfrog/artifactory/tomcat/lib

ADD http://subversion.jfrog.org/artifactory/public/trunk/distribution/standalone/src/main/install/misc/db/mysql.properties ${ARTIFACTORY_HOME}/etc/storage.properties

RUN sed -i s/localhost/mysql/ ${ARTIFACTORY_HOME}/etc/storage.properties && \
    chmod 766 ${ARTIFACTORY_HOME}/etc/storage.properties && \
    chmod 766 /opt/jfrog/artifactory/tomcat/lib/mysql-connector-java-5.1.35.jar

RUN mv $ARTIFACTORY_HOME/tomcat/conf/Catalina/localhost/artifactory.xml /tmp && \
    mv $ARTIFACTORY_HOME/tomcat/webapps/ROOT /tmp && \
    echo '<Server port="8035" shutdown="SHUTDOWN"><Service name="Catalina"><Connector port="8081"/><Engine name="Catalina" defaultHost="localhost"><Host name="localhost" appBase="/webapps"><Context path="/artifactory/" docBase="${artifactory.home}/webapps/artifactory.war" processTlds="false"><Manager pathname="" /></Context></Host></Engine></Service></Server>' > $ARTIFACTORY_HOME/tomcat/conf/server.xml

VOLUME /opt/jfrog/artifactory/logs
VOLUME /opt/jfrog/artifactory/data
VOLUME /opt/jfrog/artifactory/backup

EXPOSE 8081