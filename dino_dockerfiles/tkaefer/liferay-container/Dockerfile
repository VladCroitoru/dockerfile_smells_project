FROM openjdk:8-jdk-alpine
MAINTAINER Tobias Kaefer <tobias+lfrctnr@tkaefer.de>

RUN apk update \
  && apk add --no-cache curl bash util-linux \
  && adduser -s /bin/bash -D liferay

ENV LIFERAY_HOME=/opt/liferay

ENV CATALINA_HOME=$LIFERAY_HOME/tomcat-8.0.32

ENV PATH=$CATALINA_HOME/bin:$PATH

ENV LIFERAY_TOMCAT_URL=https://sourceforge.net/projects/lportal/files/Liferay%20Portal/7.0.2%20GA3/liferay-ce-portal-tomcat-7.0-ga3-20160804222206210.zip/download

WORKDIR /opt

RUN set -x \
            && curl -fSL "$LIFERAY_TOMCAT_URL" -o liferay-ce-portal-tomcat-7.0-ga3-20160804222206210.zip \
            && unzip liferay-ce-portal-tomcat-7.0-ga3-20160804222206210.zip \
            && rm liferay-ce-portal-tomcat-7.0-ga3-20160804222206210.zip \
            && mv /opt/liferay-ce-portal-7.0-ga3/ /opt/liferay


RUN chown -R liferay:liferay $LIFERAY_HOME

EXPOSE 8080/tcp
EXPOSE 11311/tcp

USER liferay

ENTRYPOINT ["catalina.sh", "run"]
