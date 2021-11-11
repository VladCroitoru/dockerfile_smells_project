#
# Copyright (c) 2001-2018 Primeton Technologies, Ltd.
# All rights reserved.
#
# author: ZhongWen Li (mailto:lizw@primeton.com)
#

FROM primetoninc/tomcat:7.0

# LABEL maintainer="lizw@primeton.com" \
#     provider="Primeton Technologies, Ltd."

# EOS Admin
EXPOSE 6200

ENV JAVA_OPTS="${JAVA_OPTS} -DEXTERNAL_CONFIG_DIR=${TOMCAT_HOME}/app_configs" \
    DEVOPS_DOWNLOAD_URL="ftp://product:primeton@192.168.1.12/DevOps51/dist/devops-dist/devops/files/devops.war" \
    MYSQL_DATABASE=devops \
    MYSQL_USER=devops \
    MYSQL_PASSWORD=devops \
    MYSQL_HOST=mysql

# ADD resources/devops*.war /tmp/devops.war

RUN \rm -rf ${TOMCAT_HOME}/webapps/ROOT \
    && mkdir -p ${TOMCAT_HOME}/webapps/ROOT \
    && curl --fail --location --retry 3 ${DEVOPS_DOWNLOAD_URL} \
        -o /tmp/devops.war \
    && unzip /tmp/devops.war -d ${TOMCAT_HOME}/webapps/ROOT \
    && \rm -f /tmp/devops.war \
    && curl --fail --location --retry 3 http://central.maven.org/maven2/mysql/mysql-connector-java/5.1.43/mysql-connector-java-5.1.43.jar \
        -o ${TOMCAT_HOME}/lib/mysql-connector-java-5.1.43.jar

ADD resources/user-config.xml ${TOMCAT_HOME}/webapps/ROOT/WEB-INF/_srv/config/user-config-template.xml

ADD resources/startup.conf ${TOMCAT_HOME}/app_configs/ROOT/startup.conf

ADD resources/entrypoint.sh ${TOMCAT_HOME}/bin/devops.sh

RUN chmod +x ${TOMCAT_HOME}/bin/devops.sh

ADD resources/health.html ${TOMCAT_HOME}/ROOT/health.html

HEALTHCHECK --interval=10s --timeout=5s --retries=5 \
    CMD curl -fs http://localhost:8080/health.html || exit 1

ENTRYPOINT [ "/bin/sh", "-c", "${TOMCAT_HOME}/bin/devops.sh" ]
