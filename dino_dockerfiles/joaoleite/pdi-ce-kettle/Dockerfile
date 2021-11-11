FROM openjdk:7-jdk-alpine

RUN echo 'America/Sao_Paulo' > /etc/timezone
RUN ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime

WORKDIR /opt/app

ARG KETTLE_FILE="pdi-ce-6.1.0.1-196"
ARG KETTLE_DOWNLOAD="http://downloads.sourceforge.net/project/pentaho/Data%20Integration/6.1/pdi-ce-6.1.0.1-196.zip?use_mirror=ufpr"
ARG UNZIP_KETTLE_DOWNLOAD="data-integration"
ARG NEW_NAME="kettle61"

RUN apk --update add ca-certificates openssl wget tzdata \
&& update-ca-certificates \
&& wget ${KETTLE_DOWNLOAD} -O ${KETTLE_FILE}.zip \
&& unzip ${KETTLE_FILE}.zip \
&& rm -rf ${KETTLE_FILE}.zip \
&& mkdir ${NEW_NAME} \
&& mv ${UNZIP_KETTLE_DOWNLOAD} ${NEW_NAME}

RUN mkdir /root/.kettle
COPY files/repositories.xml /root/.kettle
COPY files/entrypoint.sh /entrypoint.sh
COPY files/crontab crontab
COPY files/busybox /usr/bin/busybox
COPY files/cacerts /usr/lib/jvm/default-jvm/jre/lib/security/

RUN chmod a+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
