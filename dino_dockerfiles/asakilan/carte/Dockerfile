FROM openjdk:8-jre

MAINTAINER Ahmad Akilan

ENV ACCEPT_EULA=y

# Install MS SQL Server Tools
RUN apt-get update && \
    apt-get -y install apt-transport-https && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | tee /etc/apt/sources.list.d/msprod.list

RUN apt-get update && \
    apt-get install -y mssql-tools 

# Set required environment vars
ENV PDI_RELEASE=7.1 \
    PDI_VERSION=7.1.0.0-12 \
    CARTE_PORT=8181 \
    PENTAHO_JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 \
    PENTAHO_HOME=/opt \
    PENTAHO_DI_JAVA_OPTIONS="-Xms1024m -Xmx2048m -XX:MaxPermSize=256m -Duser.timezone=GMT"

# Create user
RUN groupadd -r pentaho && \
    useradd -s /bin/bash -d ${PENTAHO_HOME} -r -g pentaho pentaho && \
    chown pentaho:pentaho ${PENTAHO_HOME}

# Add files
RUN mkdir $PENTAHO_HOME/docker-entrypoint.d $PENTAHO_HOME/templates $PENTAHO_HOME/scripts

COPY carte-*.config.xml $PENTAHO_HOME/templates/

COPY docker-entrypoint.sh $PENTAHO_HOME/scripts/

# Download PDI
RUN /usr/bin/wget \
    --progress=dot:giga \
    'http://downloads.sourceforge.net/project/pentaho/Data%20Integration/7.0/pdi-ce-7.0.0.0-25.zip' \ 
    -O /tmp/pdi-ce-7.0.0.0-25.zip && \
    /usr/bin/unzip -q /tmp/pdi-ce-7.0.0.0-25.zip -d  $PENTAHO_HOME && \
    rm /tmp/pdi-ce-7.0.0.0-25.zip

# # install Pentaho Plugins & Libraries
# # TO Download From the Internet: 
RUN /usr/bin/wget \
    --progress=dot:giga \
    'https://download.microsoft.com/download/0/2/A/02AAE597-3865-456C-AE7F-613F99F850A8/enu/sqljdbc_6.0.8112.100_enu.tar.gz' \
    -O /tmp/sqljdbc_6.0.8112.100_enu.tar.gz && \
    tar -xvzf /tmp/sqljdbc_6.0.8112.100_enu.tar.gz -C /tmp sqljdbc_6.0/enu/jre8/sqljdbc42.jar && \
    mv /tmp/sqljdbc_6.0/enu/jre8/sqljdbc42.jar $PENTAHO_HOME/data-integration/lib/

# Expose Carte Server
EXPOSE ${CARTE_PORT}
EXPOSE 40000-40009

RUN chown -R pentaho:pentaho $PENTAHO_HOME/data-integration && \
    chmod +x $PENTAHO_HOME/scripts/docker-entrypoint.sh

# Switch to the pentaho user
USER pentaho

ENTRYPOINT ["../scripts/docker-entrypoint.sh"]

# Run Carte - these parameters are passed to the entrypoint
CMD ["carte.sh", "carte.config.xml"]