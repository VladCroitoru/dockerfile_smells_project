FROM postgres


LABEL Description="This image contains Postgres, ORACLE JDK and Atlassian Confluence" 

# Java package and other ENV
ENV JAVA_PACKAGE=server-jre \
    JAVA_VERSION_MAJOR=8 \ 
    JAVA_VERSION_MINOR=u151 \ 
    JAVA_VERSION_BUILD=b12 \
    JAVA_DIR_NAME=jdk1.8.0_151 \
    JAVA_BASE=/opt/jdk \
    PATH=${PATH}:/opt/jdk/bin \
    GLIBC_VERSION=2.23-r3 \
    LANG=C.UTF-8

# Postgres settings
ENV POSTGRES_USER=postgres \
    POSTGRES_PASSWORD=confluence \
    POSTGRES_DB=confluence 
    
# Confluence settings
ENV CONFLUENCE_USER=confluence \
	CONFLUENCE_GRP=confluence \
	CONFLUENCE_VERSION=6.5.1 \
	CONFLUENCE_HOME=/var/confluence \
	CONFLUENCE_INSTALL=/opt/atlassian/confluence 

# Using JAVA Version 8u151
ENV BASE_URL=http://download.oracle.com/otn-pub/java/jdk/8u151-b12/e758a0de34e24606bca991d704f6dcbf/${JAVA_PACKAGE}-8u151

##### JDK BASE-Urls:
## 9.0.1 => http://download.oracle.com/otn-pub/java/jdk/9.0.1+11/${JAVA_PACKAGE}-9.0.1_
## 8u151 => http://download.oracle.com/otn-pub/java/jdk/8u151-b12/e758a0de34e24606bca991d704f6dcbf/${JAVA_PACKAGE}-8u151
## 8u144 => http://download.oracle.com/otn-pub/java/jdk/8u144-b01/090f390dda5b47b9b721c7dfaa008135/${JAVA_PACKAGE}-8u144
## 8u141 => http://download.oracle.com/otn-pub/java/jdk/8u141-b15/336fa29ff2bb4ef291e347e091f7f4a7/${JAVA_PACKAGE}-8u141
## 8u131 => http://download.oracle.com/otn-pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/${JAVA_PACKAGE}-8u131
## 8u121 => http://download.oracle.com/otn-pub/java/jdk/8u121-b13/e9e7ea248e2c4826b92b3f075a80e441/${JAVA_PACKAGE}-8u121
## 8u111 => http://download.oracle.com/otn-pub/java/jdk/8u111-b14/${JAVA_PACKAGE}-8u111
## 8u101 => http://download.oracle.com/otn-pub/java/jdk/8u101-b13/${JAVA_PACKAGE}-8u101
## v8u91 => http://download.oracle.com/otn-pub/java/jdk/8u91-b14/${JAVA_PACKAGE}-8u91
## v8u77 => http://download.oracle.com/otn-pub/java/jdk/8u77-b03/${JAVA_PACKAGE}-8u77
## v8u73 => http://download.oracle.com/otn-pub/java/jdk/8u73-b02/${JAVA_PACKAGE}-8u73
## v8u71 => http://download.oracle.com/otn-pub/java/jdk/8u71-b15/${JAVA_PACKAGE}-8u71
## v8u65 => http://download.oracle.com/otn-pub/java/jdk/8u65-b17/${JAVA_PACKAGE}-8u65
## v8u60 => http://download.oracle.com/otn-pub/java/jdk/8u60-b27/${JAVA_PACKAGE}-8u60
## v8u51 => http://download.oracle.com/otn-pub/java/jdk/8u51-b16/${JAVA_PACKAGE}-8u51
## v8u45 => http://download.oracle.com/otn-pub/java/jdk/8u45-b14/${JAVA_PACKAGE}-8u45
## v8u40 => http://download.oracle.com/otn-pub/java/jdk/8u40-b25/${JAVA_PACKAGE}-8u40
## v8u31 => http://download.oracle.com/otn-pub/java/jdk/8u31-b13/${JAVA_PACKAGE}-8u31
## v8u25 => http://download.oracle.com/otn-pub/java/jdk/8u25-b17/${JAVA_PACKAGE}-8u25

RUN set -x \
    && apt-get update --quiet \
    && apt-get install --quiet --yes --no-install-recommends libtcnative-1 xmlstarlet \
    && apt-get install -y procps curl supervisor dnsutils \
    && apt-get clean 


# Install JAVA
RUN echo "Installing JDK from ${BASE_URL}" && \
    curl  -o "/tmp/java.tar.gz" -C - -LR#OH "Cookie: oraclelicense=accept-securebackup-cookie" -k "${BASE_URL}-linux-x64.tar.gz" && \
    mkdir -p ${JAVA_BASE} && \
    tar x -C ${JAVA_BASE} -f /tmp/java.tar.gz && \
    rm /tmp/java.tar.gz 

ENV JAVA_HOME=${JAVA_BASE}/${JAVA_DIR_NAME}

RUN echo "JAVA_HOME is set to ${JAVA_HOME}" && \
    update-alternatives --install /usr/bin/java java ${JAVA_HOME}/bin/java 100 && \
    update-alternatives --install /usr/bin/javac javac ${JAVA_HOME}/bin/javac 100 && \
    update-alternatives --install /usr/bin/jar jar ${JAVA_HOME}/bin/jar 100
    
# Confluence
ENV CONFLUENCE_DOWNLOAD_URL https://www.atlassian.com/software/confluence/downloads/binary/atlassian-confluence-${CONFLUENCE_VERSION}.tar.gz

# explicitly set user/group IDs
RUN groupadd -r ${CONFLUENCE_GRP} --gid=888 && useradd -r -g ${CONFLUENCE_GRP} --uid=888 ${CONFLUENCE_USER}

# Install Atlassian Confluence and helper tools and setup initial home
# directory structure.
RUN mkdir -p                              			"${CONFLUENCE_HOME}" \
    && chmod -R 700                       			"${CONFLUENCE_HOME}" \
    && chown ${CONFLUENCE_USER}:${CONFLUENCE_GRP}    "${CONFLUENCE_HOME}" \
    && mkdir -p                           			"${CONFLUENCE_INSTALL}/conf" \
    && curl -C - -LR                      			"${CONFLUENCE_DOWNLOAD_URL}" | tar -xz --directory "${CONFLUENCE_INSTALL}" --strip-components=1 --no-same-owner 
RUN chmod -R 700                       			"${CONFLUENCE_INSTALL}/conf" \
    && chmod -R 700                       			"${CONFLUENCE_INSTALL}/temp" \
    && chmod -R 700                       			"${CONFLUENCE_INSTALL}/logs" \
    && chmod -R 700                       			"${CONFLUENCE_INSTALL}/work" \
    && chown -R ${CONFLUENCE_USER}:${CONFLUENCE_GRP} "${CONFLUENCE_INSTALL}/conf" \
    && chown -R ${CONFLUENCE_USER}:${CONFLUENCE_GRP} "${CONFLUENCE_INSTALL}/temp" \
    && chown -R ${CONFLUENCE_USER}:${CONFLUENCE_GRP} "${CONFLUENCE_INSTALL}/logs" \
    && chown -R ${CONFLUENCE_USER}:${CONFLUENCE_GRP} "${CONFLUENCE_INSTALL}/work" \
    && echo -e                            "\nconfluence.home=${CONFLUENCE_HOME}" >> "${CONFLUENCE_INSTALL}/confluence/WEB-INF/classes/confluence-init.properties" \
    && xmlstarlet                         ed --inplace \
        --delete                          "Server/@debug" \
        --delete                          "Server/Service/Connector/@debug" \
        --delete                          "Server/Service/Connector/@useURIValidationHack" \
        --delete                          "Server/Service/Connector/@minProcessors" \
        --delete                          "Server/Service/Connector/@maxProcessors" \
        --delete                          "Server/Service/Engine/@debug" \
        --delete                          "Server/Service/Engine/Host/@debug" \
        --delete                          "Server/Service/Engine/Host/Context/@debug" \
                                          "${CONFLUENCE_INSTALL}/conf/server.xml" \
    && touch -d "@0"                      "${CONFLUENCE_INSTALL}/conf/server.xml"


# Supervisor config
ADD supervisor/postgres.conf supervisor/confluence.conf /etc/supervisor/conf.d/


# Expose default HTTP connector port.
EXPOSE 8090 8091 5432

# Set volume mount points for installation and home directory. Changes to the
# home directory needs to be persisted as well as parts of the installation
# directory due to eg. logs.
VOLUME ["${CONFLUENCE_INSTALL}", "${CONFLUENCE_HOME}", "${PGDATA}"]

# Set the default working directory as the Confluence installation directory.
WORKDIR ${CONFLUENCE_INSTALL}

    
CMD ["supervisord", "-n"]

