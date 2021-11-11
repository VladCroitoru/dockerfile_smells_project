FROM openjdk:8
WORKDIR /opt
ENV ARTIFACTORY_VERSION=5.4.4
ADD "https://bintray.com/jfrog/artifactory/download_file?file_path=jfrog-artifactory-oss-${ARTIFACTORY_VERSION}.zip" ./
RUN mv download_file jfrog-artifactory-oss-${ARTIFACTORY_VERSION}.zip
RUN unzip jfrog-artifactory-oss-${ARTIFACTORY_VERSION}.zip
ENV ARTIFACTORY_HOME /opt/artifactory-oss-${ARTIFACTORY_VERSION}
CMD $ARTIFACTORY_HOME/bin/artifactory.sh
#http://SERVER_DOMAIN:8081/artifactory
EXPOSE 8081
