FROM openjdk:8-slim

LABEL maintainer="geksiong@gmail.com"
LABEL description="Non-official Liferay container"

# Check if these are correct for the download file
ENV LIFERAY_VERSION=7.0-ga6
ENV TOMCAT_VERSION=8.0.32
ENV LIFERAY_TOMCAT_URL=https://sourceforge.net/projects/lportal/files/Liferay%20Portal/7.0.5%20GA6/liferay-ce-portal-tomcat-7.0-ga6-20180320170724974.zip/download

# Configuration
ENV LIFERAY_USER=liferay
ENV LIFERAY_HOME=/opt/liferay
ENV LIFERAY_BIN=${LIFERAY_HOME}/tomcat-${TOMCAT_VERSION}/bin
ENV LIFERAY_DATA=${LIFERAY_HOME}/data
ENV LIFERAY_DEPLOY=${LIFERAY_HOME}/deploy
ENV LIFERAY_LOGS=${LIFERAY_HOME}/logs

RUN apt-get update \
  && apt-get install -y curl unzip \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
  && useradd -m -d "${LIFERAY_HOME}" -s /bin/bash "${LIFERAY_USER}"

USER ${LIFERAY_USER}
WORKDIR ${LIFERAY_HOME}

RUN curl -L "$LIFERAY_TOMCAT_URL" -o liferay-ce-portal.zip \
  && unzip liferay-ce-portal.zip \
  && rm liferay-ce-portal.zip \
  && mv liferay-ce-portal-${LIFERAY_VERSION}/* . \
  && mv liferay-ce-portal-${LIFERAY_VERSION}/.[!.]* . \
  && rmdir liferay-ce-portal-${LIFERAY_VERSION}

EXPOSE 8080

VOLUME ["${LIFERAY_DATA}", "${LIFERAY_LOGS}", "${LIFERAY_DEPLOY}"]

WORKDIR ${LIFERAY_BIN}
CMD ["sh","-c","./startup.sh && tail -f /dev/null"]
