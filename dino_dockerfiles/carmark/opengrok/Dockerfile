FROM tomcat:8.0-jre8

MAINTAINER Lei Xue

RUN mkdir /src && \
  mkdir /data && \
  ln -s /data /var/opengrok && \
  ln -s /src /var/opengrok/src && \
  wget "https://github.com/oracle/opengrok/releases/download/1.0/opengrok-1.0.tar.gz" -O /tmp/opengrok-1.0.tar.gz && \
  wget "http://ftp.us.debian.org/debian/pool/main/e/exuberant-ctags/exuberant-ctags_5.9~svn20110310-8_amd64.deb" -O /tmp/exuberant-ctags_5.9-svn20110310-8_amd64.deb && \
  tar zxvf /tmp/opengrok-1.0.tar.gz -C / && \
  dpkg -i /tmp/exuberant-ctags_5.9-svn20110310-8_amd64.deb && \
  apt-get update -y && \
  apt-get -y install git && \
  apt-get -y clean && rm -fr /tmp/* /var/lib/apt/lists/* /var/cache/apk/* /var/log/*

ENV SRC_ROOT /src
ENV OPENGROK_TOMCAT_BASE /usr/local/tomcat
ENV CATALINA_HOME /usr/local/tomcat
ENV PATH $CATALINA_HOME/bin:$PATH
ENV PATH /opengrok-1.0/bin:$PATH

ENV CATALINA_BASE /usr/local/tomcat
ENV CATALINA_HOME /usr/local/tomcat
ENV CATALINA_TMPDIR /usr/local/tomcat/temp
ENV JRE_HOME /usr
ENV CLASSPATH /usr/local/tomcat/bin/bootstrap.jar:/usr/local/tomcat/bin/tomcat-juli.jar

WORKDIR $CATALINA_HOME
RUN rm -f $OPENGROK/webapps/source.jar && /opengrok-1.0/bin/OpenGrok deploy

EXPOSE 8080
ADD scripts /scripts
CMD ["/scripts/docker-entrypoint.sh"]
