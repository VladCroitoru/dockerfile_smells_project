FROM centos:centos7

MAINTAINER simon.dietschi@bluecare.ch

# Versions
ENV SONAR_VERSION 5.1.2
ENV JAVA_VERSION 8u60

# DB config, use MySQL by default
ENV SONARQUBE_JDBC_USERNAME sonar
ENV SONARQUBE_JDBC_PASSWORD sonar
ENV SONARQUBE_JDBC_URL jdbc:mysql://localhost:3306/sonar?useUnicode=true&characterEncoding=utf8&rewriteBatchedStatements=true

# Web config
ENV SONARQUBE_WEB_CONTEXT /sonar

# the home for sonar
ENV SONARQUBE_HOME /opt/sonarqube

RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys F1182E81C792928921DBCAB4CFCA4A29D26468DE

# Install requirements
RUN yum install -y wget unzip
RUN cd /opt/ \
  && wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u60-b27/jre-$JAVA_VERSION-linux-x64.rpm" \
  && yum localinstall -y jre-$JAVA_VERSION-linux-x64.rpm \
  && yum clean all \
  && rm jre-$JAVA_VERSION-linux-x64.rpm

# Install sonar
RUN set -x \
	&& cd /opt \
	&& curl -o sonarqube.zip -fSL http://downloads.sonarsource.com/sonarqube/sonarqube-$SONAR_VERSION.zip \
	&& curl -o sonarqube.zip.asc -fSL http://downloads.sonarsource.com/sonarqube/sonarqube-$SONAR_VERSION.zip.asc \
	&& gpg --verify sonarqube.zip.asc \
	&& unzip sonarqube.zip \
	&& mv sonarqube-$SONAR_VERSION sonarqube \
	&& rm sonarqube.zip* \
	&& rm -rf $SONARQUBE_HOME/bin/*

VOLUME ["$SONARQUBE_HOME/data", "$SONARQUBE_HOME/extensions"]

# http port
EXPOSE 9000

WORKDIR $SONARQUBE_HOME
COPY run.sh $SONARQUBE_HOME/bin/
RUN chmod +x $SONARQUBE_HOME/bin/run.sh

ENTRYPOINT ["./bin/run.sh"]
