FROM centos:centos6

### Upgrading system ###
RUN yum install -y tar
RUN yum -y install wget

### JDK ###
RUN wget --no-cookies --no-check-certificate --header "Cookie: oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/7u71-b14/jdk-7u71-linux-x64.rpm" -O /tmp/jdk-7-linux-x64.rpm
RUN yum -y install /tmp/jdk-7-linux-x64.rpm
ENV JAVA_HOME /usr/java/latest

### Tomcat ###
ENV CATALINA_HOME /usr/local/tomcat6
ENV PATH $CATALINA_HOME/bin:$PATH
ENV TOMCAT_MAJOR 6
ENV TOMCAT_VERSION 6.0.48
ENV TOMCAT_TGZ_URL https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-tomcat-$TOMCAT_VERSION.tar.gz
RUN curl -SL "$TOMCAT_TGZ_URL" -o /tmp/tomcat.tar.gz \
  && tar -xvf /tmp/tomcat.tar.gz -C /usr/local/ \
  && ln -s /usr/local/apache-tomcat-$TOMCAT_VERSION $CATALINA_HOME  \
  && rm -rf /tmp/tomcat.tar.gz

### Maven ###
ENV MAVEN_VERSION 3.2.3
RUN curl -sSL http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \
  && mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME /usr/share/maven

#COPY settings.xml /usr/share/maven/conf/settings.xml


