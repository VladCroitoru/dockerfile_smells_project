##Based on mdelapenya/liferay-portal:7-ce-ga3-tomcat-postgres
##Based on mdelapenya/liferay-portal:7-ce-ga3-tomcat-hsql
##Customized Java installation

FROM debian:jessie

##Java installation
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
	# update repos
	echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee /etc/apt/sources.list.d/webupd8team-java.list && \
	echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list && \
	apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 && \
	apt-get update && \
	# install java
	apt-get install oracle-java8-installer -y && \
	apt-get clean

##Base liferay installation
RUN apt-get update \
  && apt-get install -y curl \
  zip \
  #required for QBIC installation
  git \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
  && useradd -ms /bin/bash liferay

ENV LIFERAY_HOME=/usr/local/liferay-ce-portal-7.0-ga3

RUN mkdir -p "$LIFERAY_HOME"

ENV CATALINA_HOME=$LIFERAY_HOME/tomcat-8.0.32

ENV PATH=$CATALINA_HOME/bin:$PATH

ENV LIFERAY_TOMCAT_URL=https://sourceforge.net/projects/lportal/files/Liferay%20Portal/7.0.2%20GA3/liferay-ce-portal-tomcat-7.0-ga3-20160804222206210.zip/download

WORKDIR /usr/local

RUN set -x \
			&& curl -fSL "$LIFERAY_TOMCAT_URL" -o liferay-ce-portal-tomcat-7.0-ga3-20160804222206210.zip \
			&& unzip liferay-ce-portal-tomcat-7.0-ga3-20160804222206210.zip \
			&& rm liferay-ce-portal-tomcat-7.0-ga3-20160804222206210.zip

##postgresql configurations
COPY ./configs/portal-ext.properties $LIFERAY_HOME/portal-ext.properties

##QBIC customizations
COPY ./configs/qbic-ext.properties $LIFERAY_HOME/qbic-ext.properties
COPY ./configs/portlet.properties $LIFERAY_HOME/portlet.properties
COPY ./configs/labeling.methods $LIFERAY_HOME/labeling.methods

# qnavigator portlet
WORKDIR /home/liferay
RUN git clone https://github.com/qbicsoftware/qnavigator qnavigator \
    && cd qnavigator/QBiCMainPortlet/WebContent \
    && jar cvf qnavigator.war . \
    && mkdir -p $LIFERAY_HOME/deploy \
    && mv qnavigator.war $LIFERAY_HOME/deploy/

# barcode generator
# workflow portlet

##Set permissions for liferay
RUN chown -R liferay:liferay $LIFERAY_HOME

EXPOSE 8080/tcp
EXPOSE 11311/tcp

USER liferay

ENTRYPOINT ["catalina.sh", "run"]