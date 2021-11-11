FROM chrysalis69/busybox:latest
MAINTAINER chrysalis69@gmail.com

ADD https://busybox.net/downloads/binaries/ssl_helper-x86_64 /sbin/ssl_helper
RUN chmod a+x /sbin/ssl_helper
RUN ( wget --no-check-certificate --header "Cookie: oraclelicense=accept-securebackup-cookie" -O /tmp/jre.tar.gz http://download.oracle.com/otn-pub/java/jdk/8u121-b13/e9e7ea248e2c4826b92b3f075a80e441/server-jre-8u121-linux-x64.tar.gz && \
  gunzip /tmp/jre.tar.gz && \
  mkdir /opt && cd /opt && \
  tar xf /tmp/jre.tar && \
  rm /tmp/jre.tar && \
  mv /opt/jdk*/jre /opt/jre && \
  rm -rf /opt/jdk* )
RUN for cmd in $(find /opt/jre/bin/*) ; do cd /bin ; ln -s $cmd ; done
ENV JAVA_HOME /opt/jre
