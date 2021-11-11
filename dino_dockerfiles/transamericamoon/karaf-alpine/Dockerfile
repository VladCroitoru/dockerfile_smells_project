FROM java:openjdk-8-jre-alpine
MAINTAINER TRANSAMERICA_MOON

ENV JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk

ENV KARAF_VERSION=4.0.5
ENV KARAF_DATA=/data

RUN mkdir /opt; \
    cd /opt; \
    wget http://apache.openmirror.de/karaf/${KARAF_VERSION}/apache-karaf-${KARAF_VERSION}.tar.gz; \
    tar -xzf apache-karaf-${KARAF_VERSION}.tar.gz; \
    rm apache-karaf-${KARAF_VERSION}.tar.gz; \
    mv apache-karaf-${KARAF_VERSION} karaf; \
    mkdir /deploy; \
    mkdir /data; \
    sed -i 's/^\(felix\.fileinstall\.dir\s*=\s*\).*$/\1\/deploy/' /opt/karaf/etc/org.apache.felix.fileinstall-deploy.cfg; \
    sed -i 's/^sshIdleTimeout =.*$/sshIdleTimeout = 86400000/' /opt/karaf/etc/org.apache.karaf.shell.cfg; \
    sed -i '1s/.*/#\!\/bin\/ash/' /opt/karaf/bin/karaf;

VOLUME ["/deploy"]
VOLUME ["/data"]
EXPOSE 1099 8101 44444
ENTRYPOINT ["/opt/karaf/bin/karaf"]
