FROM centos:centos7

ENV JAVA_VERSION 8u31
ENV BUILD_VERSION b13

RUN yum -y update
# Install rbenv system dependencies
RUN yum install -y gcc-c++ patch readline readline-devel zlib zlib-devel libyaml-devel libffi-devel \
  openssl-devel make bzip2 autoconf automake libtool bison iconv-devel git-core 
RUN yum install -y libxslt-devel libxml2-devel ruby-devel patch
# Clean up yum cache
RUN yum clean all
# Upgrading system
RUN yum -y upgrade
RUN yum -y install wget

# Create the unprivileged application user, group and directory, and switch user
RUN groupadd builder; useradd -g builder builder --home-dir /home/builder
ENV HOME=/home/builder

# Install Ruby Version .
ARG RUBY_VERSION
ENV RUBY_VERSION=${RUBY_VERSION:-2.2.3}
COPY scripts/rbenv-setup.sh /
RUN bash /rbenv-setup.sh $RUBY_VERSION
RUN rm -fv /rbenv-setup.sh
RUN chmod -R 777 /usr/local/rbenv

ADD scripts/init.sh /usr/local/bin/init.sh 
RUN chmod +x /usr/local/bin/init.sh 
RUN chown -R builder /usr/local
RUN chown -R builder /usr/bin
RUN chmod -R 755 /usr/bin/
RUN chmod -R 777 /tmp
RUN chown builder:builder /usr/local/bin/init.sh

#============================================================
# install Java
RUN wget --no-cookies --no-check-certificate --header "Cookie: oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/$JAVA_VERSION-$BUILD_VERSION/jdk-$JAVA_VERSION-linux-x64.rpm" -O /tmp/jdk-8-linux-x64.rpm

RUN yum -y install /tmp/jdk-8-linux-x64.rpm
RUN alternatives --install /usr/bin/java jar /usr/java/latest/bin/java 200000
RUN alternatives --install /usr/bin/javaws javaws /usr/java/latest/bin/javaws 200000
RUN alternatives --install /usr/bin/javac javac /usr/java/latest/bin/javac 200000

ENV JAVA_HOME /usr/java/latest
#============================================================
# Install Maven 
ENV MAVEN_VERSION 3.3.9
RUN curl -fsSL http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn
ENV MAVEN_HOME /usr/share/maven

# Node version
ENV NODE_VERSION 4.0.0
# Installing node.js
#RUN yum install -y wget tar make gcc-c++ openssl openssl-devel
#RUN cd /tmp && wget http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION.tar.gz && tar xzf node-v$NODE_VERSION.tar.gz && cd node-#v$NODE_VERSION && ./configure && make && make install
# Installing node.js
RUN curl --silent --location https://rpm.nodesource.com/setup_4.x | bash - \
&& yum -y install nodejs

# Installing gulp and bower globally
RUN npm install -g gulp
RUN npm install -g bower
RUN chown -R builder:builder /home/builder
#RUN npm install --global --no-interactive --grunt-cli@0.1.2 gulp@3.9.0
#RUN npm install --global bower@1.4.1 --config.interactive=false
USER builder
