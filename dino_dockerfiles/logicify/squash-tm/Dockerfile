FROM logicify/centos7
MAINTAINER Dmitry Berezovsky <dmitry.berezovsky@logicify.com>

RUN yum -y install postgresql

# java7
RUN cd /opt && \
(curl -L -k -b "oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u111-b14/jdk-8u111-linux-x64.tar.gz | gunzip -c | tar x) \
 && ln -s /opt/jdk1.8.0_111 /opt/jdk8
 
ENV JAVA_HOME /opt/jdk8
ENV JRE_HOME  $JAVA_HOME/jre
ENV PATH $PATH:$JAVA_HOME/bin

USER app
RUN cd /srv  \
  && (curl -L http://www.squashtest.org/downloads/send/13-version-stable-tm/241-stm-1141-targz?lang=en | gunzip -c | tar x)

COPY startup.sh /srv/squash-tm/bin/startup.sh
COPY conf /srv/squash-tm/bin/conf
USER root
RUN chmod +x /srv/squash-tm/bin/startup.sh && chown app /srv/squash-tm/bin/conf/log4j.properties
USER app

WORKDIR /srv/squash-tm/bin
EXPOSE 8080
CMD ["./startup.sh"]
