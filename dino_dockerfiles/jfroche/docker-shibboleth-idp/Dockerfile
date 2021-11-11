FROM centos:centos6
MAINTAINER Jean-Francois Roche <jfroche@affinitic.be>

RUN yum install -y httpd mod_ssl java-1.6.0-openjdk java-1.6.0-openjdk-devel tomcat6 ntp unzip
ADD http://shibboleth.net/downloads/identity-provider/2.4.3/shibboleth-identityprovider-2.4.3-bin.zip /opt/shibboleth-identityprovider-2.4.3-bin.zip
RUN cd /opt && unzip shibboleth-identityprovider-2.4.3-bin.zip
ADD login.jsp /opt/shibboleth-identityprovider-2.4.3/src/main/webapp/
ADD login.css /opt/shibboleth-identityprovider-2.4.3/src/main/webapp/
RUN sed -i 's/idp.example.org/idp.affinitic.be/g' /opt/shibboleth-identityprovider-2.4.3/src/installer/resources/install.properties
RUN sed -i 's/keystorePassword="\${idp.keystore.pass}"/keystorePassword="CHANGEME"/g' /opt/shibboleth-identityprovider-2.4.3/src/installer/resources/build.xml
RUN cat /opt/shibboleth-identityprovider-2.4.3/src/installer/resources/build.xml
RUN export JAVA_HOME=/usr/lib/jvm/java-1.6.0 && cd /opt/shibboleth-identityprovider-2.4.3 && sh ./install.sh
ADD https://build.shibboleth.net/nexus/content/repositories/releases/edu/internet2/middleware/security/tomcat6/tomcat6-dta-ssl/1.0.0/tomcat6-dta-ssl-1.0.0.jar /usr/share/tomcat6/lib/
RUN chmod 644 /usr/share/tomcat6/lib/tomcat6-dta-ssl-1.0.0.jar
ADD server.xml /usr/share/tomcat6/conf/server.xml
ADD idp.xml /usr/share/tomcat6/conf/Catalina/localhost/idp.xml
ADD handler.xml /opt/shibboleth-idp/conf/
ADD login.config /opt/shibboleth-idp/conf/
RUN chown -R tomcat /opt/shibboleth-idp/conf
RUN chown -R tomcat /opt/shibboleth-idp/logs
RUN chown -R tomcat /opt/shibboleth-idp/metadata
RUN mkdir /usr/share/tomcat6/webapps/idp/
EXPOSE 8080 8443
CMD service tomcat6 start && tail -f /usr/share/tomcat6/logs/catalina.out
