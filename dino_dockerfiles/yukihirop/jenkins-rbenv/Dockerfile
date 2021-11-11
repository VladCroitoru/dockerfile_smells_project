# [参考] https://hub.docker.com/r/csanchez/jenkins-mysql-docker/~/dockerfile/

FROM jenkins
MAINTAINER Hiroshi Ota <otahi.pub@gmail.com>

USER root
RUN apt-get update

####################################### mysqlの環境構築

# in order to create the jenkins db
RUN apt-get -y install mysql-server libmysqlclient-dev
# install mysql plugin and repackage war
#RUN bin/mkdir -p /usr/share/jenkins
#RUN curl -sSL --create-dirs -o /tmp/WEB-INF/plugins/database.hpi https://updates.jenkins-ci.org/latest/database.hpi \
#  && curl -sSL --create-dirs -o /tmp/WEB-INF/plugins/database-mysql.hpi https://updates.jenkins-ci.org/latest/database-mysql.hpi \
#  && cd /tmp && jar cvfm /usr/share/jenkins/jenkins.war META-INF/MANIFEST.MF WEB-INF/*/* && rm -rf /tmp/WEB-INF

COPY ./jenkins-mysql.sh /usr/local/bin/jenkins-mysql.sh


####################################### rubyの環境構築

RUN apt-get install -y ruby-build
RUN groupadd ruby
RUN gpasswd -a jenkins ruby

WORKDIR /usr/local
RUN git clone https://github.com/sstephenson/rbenv.git

RUN chgrp -R ruby rbenv
RUN chmod -R g+rwxXs rbenv

RUN mkdir rbenv/plugins
WORKDIR /usr/local/rbenv/plugins
RUN git clone https://github.com/sstephenson/ruby-build.git
RUN chgrp -R ruby ruby-build
RUN chmod -R g+rwxs ruby-build

RUN echo 'export RBENV_ROOT=/usr/local/rbenv'   >> /etc/bash_profile
RUN echo 'export PATH="$RBENV_ROOT/bin:$PATH"'  >> /etc/bash_profile
RUN echo 'eval "$(rbenv init -)"'               >> /etc/bash_profile

USER jenkins

COPY plugins.txt /plugins.txt
RUN  plugins.sh /plugins.txt

EXPOSE 8888
WORKDIR $JENKINS_HOME
ENTRYPOINT ["/usr/local/bin/jenkins-mysql.sh"]
