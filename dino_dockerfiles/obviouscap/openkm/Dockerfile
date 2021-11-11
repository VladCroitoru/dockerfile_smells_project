FROM ubuntu:xenial

MAINTAINER Captain Obvious <obviouspain@gmail.com>

ENV CATALINA_HOME /usr/local/tomcat
ENV TOMCAT_VERSION 7.0.54
ENV JAVA_HOME /usr/local/java
ENV ORACLE_JAVA_HOME /usr/lib/jvm/java-8-oracle/

RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections && \
    apt-get update && \
    apt-get install -y  software-properties-common && \
    add-apt-repository -y ppa:webupd8team/java && \
    apt-get update && \
    apt-get install -y --no-install-recommends oracle-java8-installer

RUN ln -s $ORACLE_JAVA_HOME $JAVA_HOME

RUN apt-get -y install libreoffice imagemagick swftools liblog4j1.2-java libgnumail-java ant curl unzip  sudo tar nano

RUN curl -L https://downloads.sourceforge.net/project/openkm/6.3.2/openkm-6.3.2-community-tomcat-bundle.zip -o /usr/local/openkm-tomcat-bundle.zip && \
    unzip /usr/local/openkm-tomcat-bundle.zip -d /usr/local/ && rm /usr/local/openkm-tomcat-bundle.zip && ln -s $CATALINA_HOME /opt/openkm

ENV PATH $PATH:$CATALINA_HOME/bin

ADD start_openkm.sh /opt/openkm/start_openkm.sh
RUN chmod +x /opt/openkm/start_openkm.sh

EXPOSE 8080 2002

VOLUME /opt/openkm/repository

CMD /bin/bash -c "source /opt/openkm/start_openkm.sh"