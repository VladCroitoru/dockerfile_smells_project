# Extend from Alpine open-jdk
FROM jetty:9.4.7-jre8-alpine 

# Set Maintainer
LABEL authors="Vernon Chapman <g8tor692@gmail.com>"

# Set variable for later use
ENV WEBAPPS /var/lib/jetty/webapps 
ENV DATA_DIR /data/protege/webprotege
ENV PROTEGE_NAME protege 
ENV PROTEGE_VERSION 2.6.0 
ENV PROTEGE_URL https://github.com/protegeproject/webprotege/releases/download/v${PROTEGE_VERSION}/webprotege-${PROTEGE_VERSION}.war

# Become root user 
USER root

# Here we first install unzip 
# next we create directories for the application
# and data. Next, download the webprotege.war file
# and unzip it in the webapps/ROOT directory. 
RUN apk --no-cache add unzip && \
    mkdir -p ${WEBAPPS}/ROOT ${DATA_DIR} && \
    wget -O /tmp/${PROTEGE_NAME}.war $PROTEGE_URL && \
    unzip -q /tmp/${PROTEGE_NAME}.war -d ${WEBAPPS}/ROOT

# Copy configuration file
COPY config/webprotege.properties ${WEBAPPS}/ROOT/WEB-INF/classes/    

# Gfrant jetty user and group permissions
RUN chown -R jetty:jetty ${WEBAPPS} ${DATA_DIR}

# Change user to non root user
USER jetty

# Set Volume 
VOLUME [$DATA_DIR]
