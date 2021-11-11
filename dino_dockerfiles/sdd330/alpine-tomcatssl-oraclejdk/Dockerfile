FROM sdd330/alpine-tomcat-oraclejdk 

MAINTAINER Yang Leijun <yang.leijun@gmail.com>

RUN mkdir $CATALINA_HOME/cert
WORKDIR $CATALINA_HOME/cert
RUN \
  keytool -genkeypair -alias servercert -keyalg RSA -dname "CN=Web Server,OU=Unit,O=Organization,L=City,S=State,C=US" -keypass password -keystore server.jks -storepass password && \
  keytool -genkeypair -alias tomcat -keystore tomcat.p12 -storetype pkcs12 -keyalg RSA -dname "CN=tomcat,OU=Unit,O=Organization,L=City,S=State,C=US" -keypass password -storepass password && \
  keytool -exportcert -alias tomcat -file tomcat.cer -keystore tomcat.p12 -storetype pkcs12 -storepass password && \
  keytool -importcert -keystore server.jks -alias tomcat -file tomcat.cer -v -trustcacerts -noprompt -storepass password && \
  keytool -list -v -keystore server.jks -storepass password && \
  rm tomcat.cer

WORKDIR $CATALINA_HOME

COPY server.xml $CATALINA_HOME/conf/server.xml

EXPOSE 8443
