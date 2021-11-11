FROM signiant/docker-jenkins-centos-base:centos6
MAINTAINER devops@signiant.com

ENV BUILD_USER bldmgr
ENV BUILD_USER_GROUP users

# Set the timezone
RUN sed -ri '/ZONE=/c ZONE="America\/New York"' /etc/sysconfig/clock \
  && rm -f /etc/localtime \
  && ln -s /usr/share/zoneinfo/America/New_York /etc/localtime

# Install maven
ENV MAVEN_VERSION 3.2.1
RUN curl -fsSL http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \
  && mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn
ENV MAVEN_HOME /usr/share/maven

# Install yum packages required for build node
COPY yum-packages.list /tmp/yum.packages.list
RUN chmod +r /tmp/yum.packages.list \
  && yum clean all \
  && yum install -y -q `cat /tmp/yum.packages.list` \
  && yum clean all

# Install jboss, compass, node/npm, and AWS CLI -- and clear the yum cache
# NB: We have to use the fixed version of grunt-connect-proxy otherwise we get fatal socket hang up errors
RUN wget http://sourceforge.net/projects/jboss/files/JBoss/JBoss-5.1.0.GA/jboss-5.1.0.GA.zip/download -O /tmp/jboss-5.1.0.GA.zip \
  && unzip -q /tmp/jboss-5.1.0.GA.zip -d /usr/local \
  && rm -f /tmp/jboss-5.1.0.GA.zip \
  && gem update --system \
  && gem install compass \
  && npm install -g npm@latest-2 \
  && npm install -g bower grunt@0.4 grunt-cli phantomjs-prebuilt \
  && npm install -g grunt-connect-proxy@0.1.10 \
  && pip install awscli \
  && yum clean all

# Make sure anything/everything we put in the build user's home dir is owned correctly
RUN chown -R $BUILD_USER:$BUILD_USER_GROUP /home/$BUILD_USER

EXPOSE 22

# This entry will either run this container as a jenkins slave or just start SSHD
# If we're using the slave-on-demand, we start with SSH (the default)

# Default Jenkins Slave Name
ENV SLAVE_ID JAVA_NODE
ENV SLAVE_OS Linux

ADD start.sh /
RUN chmod 777 /start.sh

CMD ["sh", "/start.sh"]
