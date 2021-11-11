FROM phusion/baseimage:0.9.16

MAINTAINER Giovanni Silva giovanni@atende.info

# Java Version
ENV JAVA_VERSION_MAJOR 8
ENV JAVA_VERSION_MINOR 77
ENV JAVA_VERSION_BUILD 03
ENV JAVA_PACKAGE       server-jre

# Download and unarchive Java
RUN curl -kLOH "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie"\
  http://download.oracle.com/otn-pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz &&\
    tar -zxf ${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz -C /opt &&\
    rm ${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz &&\
    ln -s /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /opt/jdk &&\
    rm -rf /opt/jdk/*src.zip \
           /opt/jdk/lib/missioncontrol \
           /opt/jdk/lib/visualvm \
           /opt/jdk/lib/*javafx* \
           /opt/jdk/jre/lib/plugin.jar \
           /opt/jdk/jre/lib/ext/jfxrt.jar \
           /opt/jdk/jre/bin/javaws \
           /opt/jdk/jre/lib/javaws.jar \
           /opt/jdk/jre/lib/desktop \
           /opt/jdk/jre/plugin \
           /opt/jdk/jre/lib/deploy* \
           /opt/jdk/jre/lib/*javafx* \
           /opt/jdk/jre/lib/*jfx* \
           /opt/jdk/jre/lib/amd64/libdecora_sse.so \
           /opt/jdk/jre/lib/amd64/libprism_*.so \
           /opt/jdk/jre/lib/amd64/libfxplugins.so \
           /opt/jdk/jre/lib/amd64/libglass.so \
           /opt/jdk/jre/lib/amd64/libgstreamer-lite.so \
           /opt/jdk/jre/lib/amd64/libjavafx*.so \
           /opt/jdk/jre/lib/amd64/libjfx*.so

# Set environment
ENV JAVA_HOME /opt/jdk
ENV PATH $PATH:$JAVA_HOME/bin
RUN update-alternatives --install \
  /usr/bin/java      java      "$JAVA_HOME/bin/java"  200 --slave \
  /usr/bin/jar       jar       "$JAVA_HOME/bin/jar"       --slave \
  /usr/bin/jarsigner jarsigner "$JAVA_HOME/bin/jarsigner" --slave \
  /usr/bin/javac     javac     "$JAVA_HOME/bin/javac"     --slave \
  /usr/bin/javadoc   javadoc   "$JAVA_HOME/bin/javadoc"   --slave \
  /usr/bin/javah     javah     "$JAVA_HOME/bin/javah"     --slave \
  /usr/bin/javap     javap     "$JAVA_HOME/bin/javap"     --slave \
  /usr/bin/javaws    javaws    "$JAVA_HOME/bin/javaws"    --slave \
  /usr/bin/keytool   keytool   "$JAVA_HOME/bin/keytool"

COPY install_startssl-certs.sh /root/install_startssl-certs.sh
RUN /root/install_startssl-certs.sh
