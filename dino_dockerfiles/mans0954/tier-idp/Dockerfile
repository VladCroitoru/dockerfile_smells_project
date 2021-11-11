FROM   centos:7
MAINTAINER Mark McCahill "mark.mccahill@duke.edu"

USER root

RUN yum -y update &&  \
    yum -y install \
             wget \
             unzip; \
    yum clean all

ADD ./configs /build-configs
RUN cd /opt

################## start Oracle JDK ###################### 
#
#RUN wget --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie;" \
#         http://download.oracle.com/otn-pub/java/jdk/8u77-b03/jdk-8u77-linux-x64.tar.gz; \
#    mkdir /usr/local/java ; \
#    cd /usr/local/java ; \
#    tar -xzf /jdk-8u77-linux-x64.tar.gz ; \ 
#    rm /jdk-8u77-linux-x64.tar.gz ; \
#    ln -s /usr/local/java/jdk1.8.0_77 /usr/local/java/jdk 
#
#RUN echo 'export PATH="$PATH:/usr/local/java/jdk/bin"' > /etc/profile.d/java.sh ; \
#    echo 'export JAVA_HOME=/usr/local/java/jdk' >> /etc/profile.d/java.sh
#
#### Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files 8 Download
#
#RUN wget --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie;" \
#         http://download.oracle.com/otn-pub/java/jce/8/jce_policy-8.zip
#RUN cd /usr/local/java/jdk/jre/lib/security ; \
#    mv /jce_policy-8.zip /usr/local/java/jdk/jre/lib/security ; \
#    unzip jce_policy-8.zip ; \
#    mv UnlimitedJCEPolicyJDK8/* ./ ; \
#    rmdir UnlimitedJCEPolicyJDK8 ; \
#    rm jce_policy-8.zip 
#    
# gratutious symbolic link to make it easy to switch between Oracle and OpenJDK
#
#RUN mkdir /usr/local/java; \
#    ln -s  /usr/local/java/jdk /usr/java/latest
#
#
################## end Oracle JDK ################## 



################## start OpenJDK ###################### 
#
RUN yum -y update &&  \
    yum -y install \ 
             java-1.8.0-openjdk.x86_64  \
             java-1.8.0-openjdk-devel.x86_64 ;  \
    mkdir /usr/java ; \
    ln -s /etc/alternatives/java_sdk_1.8.0_openjdk /usr/java/jdk1.8.0_77 ; \
    ln -s /usr/java/jdk1.8.0_77 /usr/java/latest ; \
    yum clean all
#
################## end OpenJDK ################## 

#
# tomcat
#
RUN yum -y update &&  \
    yum -y install \
             tomcat ; \
    yum clean all

RUN yum -y update &&  \
    yum -y install \
             make \
             apr-devel \ 
             openssl-devel \
             gcc ; \
    yum clean all

#
# another tomcat, because included in CentOS 7 is too old to properly handle TLS 1.2
# and the install/config scripts I'm working from seem to depend on the old
# tomcat being installed first, so this new one can link to some of the files.
#
RUN cd /opt ; \
    wget http://apache.cs.utah.edu/tomcat/tomcat-connectors/native/1.1.34/source/tomcat-native-1.1.34-src.tar.gz ; \
    tar zxf tomcat-native-1.1.34-src.tar.gz ; \
    cd tomcat-native-1.1.34-src/jni/native ; \
    ./configure --with-apr=/usr/bin/apr-1-config --with-java-home=/usr/java/latest ; \
    make ; \
    make install 
 

RUN cd /opt ; \
    wget http://mirrors.koehn.com/apache/tomcat/tomcat-7/v7.0.68/bin/apache-tomcat-7.0.68.tar.gz ; \
    tar -zxf apache-tomcat-7.0.68.tar.gz ; \
    rm -f apache-tomcat-7.0.68.tar.gz ; \
    ln -s apache-tomcat-7.0.68 tomcat ; \
    cd tomcat ; \
    mv conf conf.default ; \
    mv logs logs.default ; \
    mv temp temp.default ; \
    mv webapps webapps.default ; \
    mv work work.default ; \
    ln -s /etc/tomcat conf ; \
    ln -s /var/log/tomcat logs ; \
    ln -s /var/cache/tomcat/temp temp ; \
    ln -s /var/lib/tomcat/webapps webapps ; \
    ln -s /var/cache/tomcat/work

RUN cp /build-configs/tomcat /etc/sysconfig/tomcat
RUN cp /build-configs/server.xml /etc/tomcat/server.xml

#
# Shibboleth IDP
#
RUN set -e ; \
    mkdir /usr/local/dist ; \
    cd /usr/local/dist ; \
    wget http://shibboleth.net/downloads/identity-provider/latest/shibboleth-identity-provider-3.2.1.tar.gz ; \
    wget http://shibboleth.net/downloads/identity-provider/latest/shibboleth-identity-provider-3.2.1.tar.gz.asc ; \
    wget http://shibboleth.net/downloads/identity-provider/latest/shibboleth-identity-provider-3.2.1.tar.gz.sha256 ; \
    wget https://shibboleth.net/downloads/PGP_KEYS ; \
    gpg --import PGP_KEYS ; \
    sha256sum --check shibboleth-identity-provider-3.2.1.tar.gz.sha256 ; \
    gpg shibboleth-identity-provider-3.2.1.tar.gz.asc ; \
    tar -xvzf shibboleth-identity-provider-3.2.1.tar.gz

RUN yum -y update &&  \
    yum -y install \
             openssl ; \
    yum clean all

#
# Install shibboleth IDP
#
RUN export JAVA_HOME=/usr/java/latest ; \
    export KEYPASS=changeit ; \
    export SEALPASS=changeit ; \
    export SCOPE=testbed.tier.internet2.edu ; \
    export HOST=idp.$SCOPE ; \
    export ENTITYID=https://$HOST/idp/shibboleth ;  \
    cd /usr/local/dist ;  \
    export DIST=/usr/local/dist/shibboleth-identity-provider-3.2.1 ; \
    export IDP_HOME=/opt/shibboleth-idp ; \
    echo \# Properties controlling the installation of the Shibboleth IdP>$DIST/idp.install.properties ; \
    export SFILE=$DIST/idp.merge.properties ; \
    echo idp.scope=$SCOPE>>$SFILE ; \
    echo idp.entityID=$ENTITYID>>$SFILE ; \
    echo idp.sealer.storePassword=$SEALPASS>>$SFILE ; \
    echo idp.sealer.keyPassword=$SEALPASS>>$SFILE ; \
    $DIST/bin/install.sh \
       -Didp.property.file=idp.install.properties \
       -Didp.merge.properties=idp.merge.properties \
       -Didp.src.dir=$DIST \
       -Didp.target.dir=$IDP_HOME \
       -Didp.scope=$SCOPE \
       -Didp.host.name=$HOST \
       -Didp.keystore.password=$KEYPASS \
       -Didp.sealer.password=$SEALPASS \
       -Didp.noprompt=true 

RUN IDP_HOME=/opt/shibboleth-idp ; \
    chgrp -R tomcat $IDP_HOME ; \
    chmod -R g+r $IDP_HOME ; \
    chmod g+w $IDP_HOME/logs ; \
    chmod g+s $IDP_HOME/logs

#
# Install Java Server Tag Library
#
RUN wget https://build.shibboleth.net/nexus/service/local/repositories/thirdparty/content/javax/servlet/jstl/1.2/jstl-1.2.jar \
          -P /usr/share/tomcat/lib/


#
# Deploy to Tomcat
#
RUN cp /build-configs/idp.xml /etc/tomcat/Catalina/localhost/

#
# configs galore
#
RUN cp /build-configs/password-authn-config.xml /opt/shibboleth-idp/conf/authn/password-authn-config.xml
RUN cp /build-configs/krb5-authn-config.xml /opt/shibboleth-idp/conf/authn/krb5-authn-config.xml
RUN cp /build-configs/metadata-providers.xml /opt/shibboleth-idp/conf/metadata-providers.xml
RUN cp /build-configs/attribute-resolver.xml /opt/shibboleth-idp/conf/attribute-resolver.xml
RUN cp /build-configs/ldap.properties /opt/shibboleth-idp/conf/ldap.properties
RUN cp /build-configs/attribute-filter.xml /opt/shibboleth-idp/conf/attribute-filter.xml
RUN cp /build-configs/inc-md-cert.pem /opt/shibboleth-idp/credentials/inc-md-cert.pem 
RUN chown root:tomcat /opt/shibboleth-idp/credentials/inc-md-cert.pem 
RUN chmod 644 /opt/shibboleth-idp/credentials/inc-md-cert.pem
RUN chmod 775 /opt/shibboleth-idp/metadata


#
# things we need assuming we end up running systemd
#
ENV container docker
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;
VOLUME [ "/sys/fs/cgroup" ]

RUN systemctl enable tomcat.service

EXPOSE 8080 8443 443
CMD ["/usr/sbin/init"]