# Multistage build
# We need to build damsrepo first and then copy the war to tomcat
FROM openjdk:8-alpine as damsrepo-builder
MAINTAINER "Matt Critchlow <mcritchlow@ucsd.edu">

RUN apk add --no-cache apache-ant git unzip
RUN git clone https://github.com/ucsdlib/damsrepo.git /tmp/damsrepo
WORKDIR /tmp/damsrepo
RUN ant webapp
RUN mkdir -p /pub/dams
RUN mv /tmp/damsrepo/dist/dams.war /pub/dams/
RUN mv /tmp/damsrepo/src/properties/jhove.conf /pub/dams/
RUN mv /tmp/damsrepo/src/lib2/postgresql-9.2-1002.jdbc4.jar /pub/dams/

# Get fits
ENV FITS_VERSION 1.3.0
RUN wget https://projects.iq.harvard.edu/files/fits/files/fits-$FITS_VERSION.zip \
    && unzip fits-$FITS_VERSION.zip -d /usr/local/bin/fits \
    && chmod 0755 /usr/local/bin/fits/fits.sh \
    && rm fits-$FITS_VERSION.zip

# Get dockerize
ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

FROM tomcat:7-jre8-alpine
MAINTAINER "Matt Critchlow <mcritchlow@ucsd.edu">

# Environment defaults. Obviously, uh, *development*
ENV MANAGER_USER tomcat
ENV MANAGER_PASS tomcat
ENV DAMS_USER dams
ENV DAMS_PASS dams

RUN apk add --no-cache openssl imagemagick ffmpeg

# install dockerize
COPY --from=damsrepo-builder /usr/local/bin/dockerize /usr/local/bin/dockerize
# install fits
COPY --from=damsrepo-builder /usr/local/bin/fits /usr/local/bin/fits

# setup config and other required files
COPY tomcat/tomcat-users.xml /usr/local/tomcat/conf/tomcat-users.xml
COPY tomcat/server.xml /usr/local/tomcat/conf/server.xml

# Install damsrepo and friends
RUN mkdir -p /pub/dams/editBackups
RUN mkdir -p /pub/dams/xsl
COPY damsrepo/xsl /pub/dams/xsl/
COPY damsrepo/dams.properties /pub/dams/dams.properties
COPY --from=damsrepo-builder /pub/dams/jhove.conf /pub/dams/jhove.conf
COPY --from=damsrepo-builder /pub/dams/postgresql-9.2-1002.jdbc4.jar /usr/local/tomcat/lib/postgresql-9.2-1002.jdbc4.jar
COPY --from=damsrepo-builder /pub/dams/dams.war /usr/local/tomcat/webapps/
