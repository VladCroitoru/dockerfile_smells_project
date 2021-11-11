FROM centos:centos7

MAINTAINER David King <dsmk@bu.edu>

ENV JRE_HOME /opt/jre1.8.0_60
ENV JAVA_HOME /opt/jre1.8.0_60
ENV JETTY_HOME /opt/jetty
ENV JETTY_BASE /opt/iam-jetty-base
# this change was necessary for eduGAIN data
#ENV JETTY_MAX_HEAP 512m
ENV JETTY_MAX_HEAP 1024m
ENV PATH $PATH:$JRE_HOME/bin:/opt/container-scripts:/opt/shibboleth/bin

RUN yum -y update \
    && yum -y install wget tar unzip openssl

# Download Java, verify the hash, and install
RUN set -x; \
    java_version=8u60; \
    wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" \
    http://download.oracle.com/otn-pub/java/jdk/$java_version-b27/jre-$java_version-linux-x64.tar.gz \
    && echo "49dadecd043152b3b448288a35a4ee6f3845ce6395734bacc1eae340dff3cbf5  jre-$java_version-linux-x64.tar.gz" | sha256sum -c - \
    && tar -zxvf jre-$java_version-linux-x64.tar.gz -C /opt \
    && rm jre-$java_version-linux-x64.tar.gz 

# Add support for the unlimited 
RUN set -x; \
  jce_version=8; \
  wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" \
  "http://download.oracle.com/otn-pub/java/jce/$jce_version/jce_policy-$jce_version.zip" \
  && echo "f3020a3922efd6626c2fff45695d527f34a8020e938a49292561f18ad1320b59 jce_policy-$jce_version.zip" | sha256sum -c - \
  && unzip jce_policy-$jce_version.zip -d /opt \
  && mv "${JAVA_HOME}/lib/security/local_policy.jar" "/opt/UnlimitedJCEPolicyJDK8/local_policy.jar-strong" \
  && mv "${JAVA_HOME}/lib/security/US_export_policy.jar" "/opt/UnlimitedJCEPolicyJDK8/US_export_policy.jar-strong" \
  && cp -p /opt/UnlimitedJCEPolicyJDK8/US_export_policy.jar  "${JAVA_HOME}/lib/security/US_export_policy.jar" \
  && cp -p /opt/UnlimitedJCEPolicyJDK8/local_policy.jar  "${JAVA_HOME}/lib/security/local_policy.jar" 
  

#http://ftp.ussg.iu.edu/eclipse/jetty/9.3.6.v20151106/dist/jetty-distribution-9.3.6.v20151106.zip
# Download Jetty, verify the hash, and install, initialize a new base
RUN set -x; \
    jetty_version=9.3.6.v20151106; \
    wget -O jetty.zip "https://eclipse.org/downloads/download.php?file=/jetty/$jetty_version/dist/jetty-distribution-$jetty_version.zip&r=1" \
    && echo "9cc0220a8eb75c68c1d655fe8087ce303b10030011c138357e3f31f38d83f148  jetty.zip" | sha256sum -c - \
    && unzip jetty.zip -d /opt \
    && mv /opt/jetty-distribution-$jetty_version /opt/jetty \
    && rm jetty.zip \
    && cp /opt/jetty/bin/jetty.sh /etc/init.d/jetty \
    && mkdir -p /opt/iam-jetty-base/modules \
    && mkdir -p /opt/iam-jetty-base/lib/ext \
    && mkdir -p /opt/iam-jetty-base/resources \
    && cd /opt/iam-jetty-base \
    && touch start.ini \
    && $JRE_HOME/bin/java -jar ../jetty/start.jar --add-to-startd=http,https,deploy,ext,annotations,jstl,logging,setuid \
    && sed -i 's/# jetty.http.port=8080/jetty.http.port=80/g' /opt/iam-jetty-base/start.d/http.ini \
    && sed -i 's/# jetty.ssl.port=8443/jetty.ssl.port=443/g' /opt/iam-jetty-base/start.d/ssl.ini \
    && sed -i 's/<New id="DefaultHandler" class="org.eclipse.jetty.server.handler.DefaultHandler"\/>/<New id="DefaultHandler" class="org.eclipse.jetty.server.handler.DefaultHandler"><Set name="showContexts">false<\/Set><\/New>/g' /opt/jetty/etc/jetty.xml

# set up an existing /opt/shibboleth-idp directory so we will upgrade install
#RUN mkdir /opt/shibboleth-idp
#ADD bu/shib1/ /opt/shibboleth-idp/

# Download Shibboleth IdP, verify the hash, and install
ADD bu-install.sh /opt/bu-install.sh
RUN chmod 755 /opt/bu-install.sh \
  && /opt/bu-install.sh

# Download the library to allow SOAP Endpoints, verify the hash, and place
#RUN set -x; \
#    wget https://build.shibboleth.net/nexus/content/repositories/releases/net/shibboleth/utilities/jetty9/jetty9-dta-ssl/1.0.0/jetty9-dta-ssl-1.0.0.jar \
#    && echo "2f547074b06952b94c35631398f36746820a7697  jetty9-dta-ssl-1.0.0.jar" | sha1sum -c - \
#    && mv jetty9-dta-ssl-1.0.0.jar /opt/iam-jetty-base/lib/ext/

ADD iam-jetty-base/ /opt/iam-jetty-base/

# Clean up the install
#RUN yum -y remove wget tar unzip; yum clean all

RUN useradd jetty -U -s /bin/false \
    && mkdir /opt/shibboleth-idp/metadata-cache \
    && chown -R jetty:root /opt/jetty \
    && chown -R jetty:root /opt/iam-jetty-base \
    && chown -R jetty:root /opt/shibboleth-idp/logs /opt/shibboleth-idp/metadata-cache

ADD container-scripts/ /opt/container-scripts/

RUN chmod -R +x /opt/container-scripts/

## Opening 443 (browser TLS), 8443 (SOAP/mutual TLS auth)... 80 specifically not included.
# We only do 443 at Boston University
EXPOSE 443 

VOLUME ["/external-mount"]

CMD ["run-shibboleth.sh"]

# these are only in here to simplify our build - we should actually put these in 
# a separate Docker file
#FROM dsmk/shibboleth-idp

#ADD bu/conf/ /opt/shibboleth-idp/conf/
#ADD bu/credentials/ /opt/shibboleth-idp/credentials/
#ADD bu/metadata/ /opt/shibboleth-idp/metadata/
#ADD bu/webapp/ /opt/shibboleth-idp/webapp/

#ADD bu/keystore $JETTY_BASE/etc/keystore

