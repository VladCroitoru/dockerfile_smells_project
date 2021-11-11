# WebApollo
# VERSION 2.0
FROM tomcat:8-jre8
MAINTAINER Eric Rasche <esr@tamu.edu>, Anthony Bretaudeau <anthony.bretaudeau@inria.fr>, Nathan Dunn <nathandunn@lbl.gov>
ENV DEBIAN_FRONTEND noninteractive 

RUN apt-get -qq update --fix-missing && \
	apt-get --no-install-recommends -y install \
	git build-essential maven tomcat8 libpq-dev postgresql-common openjdk-8-jdk wget \
	postgresql postgresql-client xmlstarlet netcat libpng-dev zlib1g-dev libexpat1-dev ant curl ssl-cert

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get -qq update --fix-missing && \
	apt-get --no-install-recommends -y install nodejs && \
	apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN cp /usr/lib/jvm/java-8-openjdk-amd64/lib/tools.jar /usr/lib/jvm/java-8-openjdk-amd64/jre/lib/ext/tools.jar && \
	useradd -ms /bin/bash -d /apollo apollo

ENV WEBAPOLLO_VERSION master 
RUN curl -L https://github.com/GMOD/Apollo/archive/${WEBAPOLLO_VERSION}.tar.gz | tar xzf - --strip-components=1 -C /apollo


COPY build.sh /bin/build.sh
ADD apollo-config.groovy /apollo/apollo-config.groovy

RUN chown -R apollo:apollo /apollo
USER apollo
RUN bash /bin/build.sh
USER root

ENV CATALINA_HOME=/usr/local/tomcat/
RUN rm -rf ${CATALINA_HOME}/webapps/* && \
	cp /apollo/apollo*.war ${CATALINA_HOME}/apollo.war

ENV CONTEXT_PATH ROOT

# setup TomCat SSL on 8443
RUN keytool -genkey -validity 365 -alias tomcat -keyalg RSA -storepass changeit -keypass changeit -dname "CN=WormBase,OU=ParaSite,O=EMBL-EBI,L=Cambridge,ST=Cambridgeshire,C=UK"
RUN sed -i 's/<Service name="Catalina">/<Service name="Catalina">\n\n    <Connector port="8443" protocol="org.apache.coyote.http11.Http11NioProtocol"\n        maxThreads="25" SSLEnabled="true" scheme="https" secure="true"\n        clientAuth="false" sslProtocol="TLS" acceptCount="100" keystoreFile="\/root\/.keystore" keystorePass="changeit"\/>/' ${CATALINA_HOME}/conf/server.xml
RUN sed -i 's/redirectPort="8443"//g' ${CATALINA_HOME}/conf/server.xml

# Download chado schema
RUN wget --quiet https://github.com/erasche/chado-schema-builder/releases/download/1.31-jenkins97/chado-1.31.sql.gz -O /chado.sql.gz && \
	gunzip /chado.sql.gz

ADD launch.sh /launch.sh
CMD "/launch.sh"


