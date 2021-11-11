FROM centos:5.11
RUN useradd -c "JBoss" -m jboss -s /bin/bash -d /opt/jboss; \
    passwd -d jboss; \
    yum install -y unzip curl nano telnet; \
    curl -LO 'http://download.oracle.com/otn-pub/java/jdk/7u51-b13/jdk-7u51-linux-x64.rpm' -H 'Cookie: oraclelicense=accept-securebackup-cookie'; \
    rpm -i jdk-7u51-linux-x64.rpm
COPY jboss-eap-6.1.0.zip* /opt/jboss/
WORKDIR /opt/jboss
RUN cat jboss-eap-6.1.0.zipaa jboss-eap-6.1.0.zipab jboss-eap-6.1.0.zipac > jboss-eap-6.1.0.zip; \
    unzip jboss-eap-6.1.0.zip; \
    mv jboss-eap-6.1/* .; \
    rm -r jboss-eap-6.1.0.zip* jboss-eap-6.1; \
    chown -R jboss:jboss /opt/jboss; \
    chown jboss:jboss /opt/jboss/standalone/deployments
USER jboss
EXPOSE 8080 9990
ENV JAVA_HOME /usr/java/jdk1.7.0_51
ENV PATH $JAVA_HOME/bin:$PATH
ENV JBOSS_HOME /opt/jboss
VOLUME /opt/jboss/standalone/deployments
CMD ["/opt/jboss/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0"]
