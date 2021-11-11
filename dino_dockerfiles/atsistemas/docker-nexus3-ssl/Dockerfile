FROM sonatype/docker-nexus3:3.0.2

MAINTAINER Manuel Valle <mvalle@atsistemas.com>


ENV NEXUS_KEYSTORE /nexus-keystore
ENV KEYSTOREPASSWORD=changeit
ENV KEYMANAGERPASSWORD=changeit
ENV TRUSTSTOREPASSWORD=changeit

USER root
RUN mkdir -p ${NEXUS_KEYSTORE} && chown nexus:nexus ${NEXUS_KEYSTORE}

EXPOSE 8443

RUN /opt/java/bin/keytool -genkeypair \
        -keystore ${NEXUS_KEYSTORE}/keystore.jks \
        -storepass changeit \
        -keypass changeit \
        -alias jetty -keyalg RSA -keysize 2048 -validity 5000  \
        -dname "CN=*.local, OU=Example, O=Sonatype, L=Unspecified, ST=Unspecified, C=US" \
        -ext "SAN=DNS:nexus.local" -ext "BC=ca:true"

RUN sed  's|\(nexus-args=.*\)|\1,${karaf.etc}/jetty-https.xml|' -i /opt/sonatype/nexus/etc/org.sonatype.nexus.cfg \
     && echo 'application-port-ssl=8443' >> /opt/sonatype/nexus/etc/org.sonatype.nexus.cfg \
     && sed 's|\(<Set name="KeyStorePath">\).*$|\1<Env name="NEXUS_KEYSTORE"/>/keystore.jks</Set>|' \
        -i /opt/sonatype/nexus/etc/jetty-https.xml \
     && sed 's|\(<Set name="KeyStorePassword">\).*$|\1<Env name="KEYSTOREPASSWORD"/></Set>|' \
        -i /opt/sonatype/nexus/etc/jetty-https.xml \
     && sed 's|\(<Set name="KeyManagerPassword">\).*$|\1<Env name="KEYMANAGERPASSWORD"/></Set>|' \
        -i /opt/sonatype/nexus/etc/jetty-https.xml \
     && sed 's|\(<Set name="TrustStorePath">\).*$|\1<Env name="NEXUS_KEYSTORE"/>/keystore.jks</Set>|' \
        -i /opt/sonatype/nexus/etc/jetty-https.xml \
     && sed 's|\(<Set name="TrustStorePassword">\).*$|\1<Env name="TRUSTSTOREPASSWORD"/></Set>|' \
        -i /opt/sonatype/nexus/etc/jetty-https.xml

USER nexus
