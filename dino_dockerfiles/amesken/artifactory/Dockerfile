FROM tomcat:8.0.29-jre8

MAINTAINER Andries Mesken <andries.mesken@ziggo.nl>

# To update, check https://bintray.com/jfrog/artifactory/jfrog-artifactory-oss-zip/view (or for pro version
#  https://bintray.com/jfrog/artifactory-pro/jfrog-artifactory-pro-zip/view)
ENV ARTIFACTORY_VERSION 4.3.0
ENV ARTIFACTORY_SHA1 e8f558dcf0ebae02c54cf82ebbcfbf7563bba492

# Disable Tomcat's manager application.
RUN rm -rf webapps/*

# Redirect URL from / to artifactory/ using UrlRewriteFilter
COPY urlrewrite/WEB-INF/lib/urlrewritefilter.jar /
COPY urlrewrite/WEB-INF/urlrewrite.xml /
RUN \
  mkdir -p webapps/ROOT/WEB-INF/lib && \
  mv /urlrewritefilter.jar webapps/ROOT/WEB-INF/lib && \
  mv /urlrewrite.xml webapps/ROOT/WEB-INF/

# Fetch and install Artifactory OSS war archive.
RUN \
  echo $ARTIFACTORY_SHA1 artifactory.zip > artifactory.zip.sha1 && \
  curl -L -o artifactory.zip https://bintray.com/artifact/download/jfrog/artifactory/jfrog-artifactory-oss-${ARTIFACTORY_VERSION}.zip && \
#  PRO VERSIE https://bintray.com/artifact/download/jfrog/artifactory-pro/org/artifactory/pro/jfrog-artifactory-pro/${ARTIFACTORY_VERSION}/jfrog-artifactory-pro-${ARTIFACTORY_VERSION}.zip
  sha1sum -c artifactory.zip.sha1 && \
  unzip -j artifactory.zip "artifactory-*/webapps/artifactory.war" -d webapps && \
  rm artifactory.zip

# Expose tomcat runtime options through the RUNTIME_OPTS environment variable.
#   Example to set the JVM's max heap size to 256MB use the flag
#   '-e RUNTIME_OPTS="-Xmx256m"' when starting a container.
RUN echo 'export CATALINA_OPTS="$RUNTIME_OPTS"' > bin/setenv.sh

# Artifactory home
RUN mkdir -p /artifactory
ENV ARTIFACTORY_HOME /artifactory

# creeer en zet rechten op local data folders
RUN mkdir -p /c/Users/Andries/docker/data/artifactory/data && chmod 777 /c/Users/Andries/docker/data/artifactory/data && \
  mkdir -p /c/Users/Andries/docker/data/artifactory/logs && chmod 777 /c/Users/Andries/docker/data/artifactory/logs && \
  mkdir -p /c/Users/Andries/docker/data/artifactory/backup && chmod 777 /c/Users/Andries/docker/data/artifactory/backup
  
# Expose Artifactories data, log and backup directory.
VOLUME ["$ARTIFACTORY_HOME/data", "$ARTIFACTORY_HOME/logs", "$ARTIFACTORY_HOME/backup"]

WORKDIR $ARTIFACTORY_HOME

EXPOSE 8081