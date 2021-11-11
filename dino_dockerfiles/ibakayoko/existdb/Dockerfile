FROM openjdk:8-jre
MAINTAINER Ibrahim Bakayoko 
#Releases https://bintray.com/existdb/releases/exist
ENV EXIST_DB_VERSION 3.5.0
ENV EXIST_HOME /opt/existdb
ENV EXIST_PASSWORD 0000
ENV MAX_MEMORY 2048
ENV DEFAULT_COLLECTION mycollection

# eXistDB needs ant to automate common tasks like backup/restore or importing
RUN apt-get update; apt-get -y install expect; apt-get clean

# install exist and cleanup
RUN wget -q -O '/opt/exist.jar' https://bintray.com/artifact/download/existdb/releases/eXist-db-setup-$EXIST_DB_VERSION.jar

ADD exist-setup.cmd /opt/exist-setup.cmd
ADD entrypoint.sh /entrypoint.sh

#Solr Analayzer Conf File
ADD conf/collection.xconf /opt/collection.xconf

VOLUME ${EXIST_HOME}/webapp/WEB-INF/data/
EXPOSE 8080 8443

CMD ["/entrypoint.sh"]