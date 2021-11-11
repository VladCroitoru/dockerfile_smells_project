FROM java:openjdk-7 
#FROM busybox

MAINTAINER Markus Gritsch

ENV JAVA_VERSION=7u79
ENV KARAF_VERSION=2.3.11

ENV KARAF_DEBUG true
EXPOSE 1099 8101 44444 5005

#RUN wget http://apache.openmirror.de/karaf/${KARAF_VERSION}/apache-karaf-${KARAF_VERSION}.tar.gz; \
#    mkdir /opt/karaf; \
#    tar --strip-components=1 -C /opt/karaf -xzf apache-karaf-${KARAF_VERSION}.tar.gz; \
#    rm apache-karaf-${KARAF_VERSION}.tar.gz; \
#    mkdir /deploy; \
#    sed -i 's/^\(felix\.fileinstall\.dir\s*=\s*\).*$/\1\/deploy/' /opt/karaf/etc/org.apache.felix.fileinstall-deploy.cfg

RUN mkdir /tmpDeploy
RUN mkdir /deploy

RUN wget --no-check-certificate --no-cookies \
    --header "Cookie: oraclelicense=accept-securebackup-cookie" \
    http://download.oracle.com/otn-pub/java/jdk/${JAVA_VERSION}-b15/jre-${JAVA_VERSION}-macosx-x64.tar.gz -O /tmpDeploy/jre.tar.gz && \
    mkdir /tmpDeploy/jre && \
    tar xzf /tmpDeploy/jre.tar.gz -C /tmpDeploy/jre

RUN wget http://apache.openmirror.de/karaf/${KARAF_VERSION}/apache-karaf-${KARAF_VERSION}.tar.gz -O /tmpDeploy/karaf.tar.gz && \
    mkdir /tmpDeploy/karaf && \
    tar xzf /tmpDeploy/karaf.tar.gz -C /tmpDeploy/karaf

#VOLUME ["/deploy"]

#COPY tmpDeploy deploy

RUN cp -r /tmpDeploy/jre/ /deploy
RUN cp -r /tmpDeploy/karaf/ /deploy

VOLUME ["/deploy"]

#ENTRYPOINT ["/bin/cp","-r", "/tmp/iso/boot","/data"]

#CMD ["./opt/karaf/bin/karaf"]
CMD /bin/sh
