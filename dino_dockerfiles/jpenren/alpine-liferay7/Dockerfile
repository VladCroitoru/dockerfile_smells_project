FROM jpenren/alpine-openjdk8

MAINTAINER Javier Pena

ENV LFR_VERSION 7.0-ce-ga1
ENV PACKAGE liferay-portal-tomcat-$LFR_VERSION-20160331161017956.zip

RUN wget -P /tmp/ http://downloads.sourceforge.net/project/lportal/Liferay%20Portal/7.0.0%20GA1/$PACKAGE &&\
    mkdir -p /opt &&\
    unzip /tmp/$PACKAGE -d /opt/ -x "liferay-portal-7.0-ce-ga1/work/*" -x "liferay-portal-7.0-ce-ga1/tomcat-8.0.32/work/*" &&\
    rm /tmp/$PACKAGE &&\
    mv /opt/liferay-portal-$LFR_VERSION /opt/liferay-portal

COPY portal-setup-wizard.properties /opt/liferay-portal/

VOLUME /opt/liferay-portal/data

EXPOSE 8080

CMD ["/opt/liferay-portal/tomcat-8.0.32/bin/catalina.sh", "run"]
