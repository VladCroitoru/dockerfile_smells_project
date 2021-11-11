# Official images are cool.
FROM jenkins
MAINTAINER Alex Vo <tuanmaster2012@gmail.com>

# Jenkins is using jenkins user, we need root to install things.
USER root

RUN mkdir -p /tmp/WEB-INF/plugins

# Install required jenkins plugins.
RUN curl -L https://updates.jenkins-ci.org/latest/checkstyle.hpi -o /tmp/WEB-INF/plugins/checkstyle.hpi && \
  curl -L https://updates.jenkins-ci.org/latest/cloverphp.hpi -o /tmp/WEB-INF/plugins/cloverphp.hpi && \
  curl -L https://updates.jenkins-ci.org/latest/crap4j.hpi -o /tmp/WEB-INF/plugins/crap4j.hpi && \
  curl -L https://updates.jenkins-ci.org/latest/dry.hpi -o /tmp/WEB-INF/plugins/dry.hpi && \
  curl -L https://updates.jenkins-ci.org/latest/htmlpublisher.hpi -o /tmp/WEB-INF/plugins/htmlpublisher.hpi && \
  curl -L https://updates.jenkins-ci.org/latest/jdepend.hpi -o /tmp/WEB-INF/plugins/jdepend.hpi && \
  curl -L https://updates.jenkins-ci.org/latest/plot.hpi -o /tmp/WEB-INF/plugins/plot.hpi && \
  curl -L https://updates.jenkins-ci.org/latest/pmd.hpi -o /tmp/WEB-INF/plugins/pmd.hpi && \
  curl -L https://updates.jenkins-ci.org/latest/violations.hpi -o /tmp/WEB-INF/plugins/violations.hpi && \
  curl -L https://updates.jenkins-ci.org/latest/xunit.hpi -o /tmp/WEB-INF/plugins/xunit.hpi && \
  curl -L https://updates.jenkins-ci.org/latest/git-client.hpi -o /tmp/WEB-INF/plugins/git-client.hpi && \
  curl -L https://updates.jenkins-ci.org/latest/scm-api.hpi -o /tmp/WEB-INF/plugins/scm-api.hpi && \
  curl -L https://updates.jenkins-ci.org/latest/git.hpi -o /tmp/WEB-INF/plugins/git.hpi && \
  curl -L https://updates.jenkins-ci.org/latest/bitbucket.hpi -o /tmp/WEB-INF/plugins/bitbucket.hpi && \
  curl -L https://updates.jenkins-ci.org/latest/publish-over-ssh.hpi -o /tmp/WEB-INF/plugins/publish-over-ssh.hpi && \
  curl -L https://updates.jenkins-ci.org/latest/greenballs.hpi -o /tmp/WEB-INF/plugins/greenballs.hpi && \
  curl -L https://updates.jenkins-ci.org/latest/htmlpublisher.hpi -o /tmp/WEB-INF/plugins/htmlpublisher.hpi && \
  curl -L https://updates.jenkins-ci.org/latest/workflow-aggregator.hpi -o /tmp/WEB-INF/plugins/workflow-aggregator.hpi && \
  curl -L https://updates.jenkins-ci.org/latest/ansicolor.hpi -o /tmp/WEB-INF/plugins/ansicolor.hpi

# Install Docker plugin for docker deploy.
RUN curl -L https://updates.jenkins-ci.org/latest/docker-build-publish.hpi -o /tmp/WEB-INF/plugins/docker-build-publish.hpi

# Add all to the war file.
RUN cd /tmp; \
  zip --grow /usr/share/jenkins/jenkins.war WEB-INF/plugins/checkstyle.hpi && \
  zip --grow /usr/share/jenkins/jenkins.war WEB-INF/plugins/cloverphp.hpi && \
  zip --grow /usr/share/jenkins/jenkins.war WEB-INF/plugins/crap4j.hpi && \
  zip --grow /usr/share/jenkins/jenkins.war WEB-INF/plugins/dry.hpi && \
  zip --grow /usr/share/jenkins/jenkins.war WEB-INF/plugins/htmlpublisher.hpi && \
  zip --grow /usr/share/jenkins/jenkins.war WEB-INF/plugins/jdepend.hpi && \
  zip --grow /usr/share/jenkins/jenkins.war WEB-INF/plugins/plot.hpi && \
  zip --grow /usr/share/jenkins/jenkins.war WEB-INF/plugins/pmd.hpi && \
  zip --grow /usr/share/jenkins/jenkins.war WEB-INF/plugins/violations.hpi && \
  zip --grow /usr/share/jenkins/jenkins.war WEB-INF/plugins/xunit.hpi && \
  zip --grow /usr/share/jenkins/jenkins.war WEB-INF/plugins/docker-build-publish.hpi && \
  zip --grow /usr/share/jenkins/jenkins.war WEB-INF/plugins/git-client.hpi && \
  zip --grow /usr/share/jenkins/jenkins.war WEB-INF/plugins/scm-api.hpi && \
  zip --grow /usr/share/jenkins/jenkins.war WEB-INF/plugins/git.hpi && \
  zip --grow /usr/share/jenkins/jenkins.war WEB-INF/plugins/bitbucket.hpi && \
  zip --grow /usr/share/jenkins/jenkins.war WEB-INF/plugins/publish-over-ssh.hpi && \
  zip --grow /usr/share/jenkins/jenkins.war WEB-INF/plugins/greenballs.hpi && \
  zip --grow /usr/share/jenkins/jenkins.war WEB-INF/plugins/htmlpublisher.hpi && \
  zip --grow /usr/share/jenkins/jenkins.war WEB-INF/plugins/workflow-aggregator.hpi && \
  zip --grow /usr/share/jenkins/jenkins.war WEB-INF/plugins/ansicolor.hpi

# Install php packages.
RUN apt-get update
RUN apt-get -y -f install php5-cli php5-dev php5-curl curl php-pear ant

# Install php xdebug extension for code coverage
# Setup the Xdebug version to install
ENV XDEBUG_VERSION 2.3.3
ENV XDEBUG_MD5 60e6fdf41840104a23debe16db15a2af

# Install Xdebug
RUN set -x \
     && curl -SL "http://www.xdebug.org/files/xdebug-$XDEBUG_VERSION.tgz" -o xdebug.tgz \
     && echo $XDEBUG_MD5 xdebug.tgz | md5sum -c - \
     && mkdir -p /usr/src/xdebug \
     && tar -xf xdebug.tgz -C /usr/src/xdebug --strip-components=1 \
     && rm xdebug.* \
     && cd /usr/src/xdebug \
     && phpize \
     && ./configure \
     && make -j"$(nproc)" \
     && make install \
     && make clean

COPY ext-xdebug.ini /etc/php5/mods-available/
COPY ext-xdebug.ini /etc/php5/cli/conf.d/


# Install docker
RUN apt-get -y -f install docker.io

# Create a jenkins "HOME" for composer files.
RUN mkdir /home/jenkins
RUN chown jenkins:jenkins /home/jenkins

USER jenkins

#### This don't work as $JENKINS_HOME is a volume ####
# Install php template.
#RUN mkdir "$JENKINS_HOME/jobs/php-template"
#RUN curl -L https://raw.github.com/sebastianbergmann/php-jenkins-template/master/config.xml -o "$JENKINS_HOME/jobs/php-template/config.xml"
####                sad panda is sad              ####


# Install composer, yes we can't install it in $JENKINS_HOME :(
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/home/jenkins

# Install required php tools.
RUN /home/jenkins/composer.phar --working-dir="/home/jenkins" -n require phing/phing:2.* notfloran/phing-composer-security-checker:~1.0 \
    phploc/phploc:* phpunit/phpunit:~4.0 pdepend/pdepend:~2.0 phpmd/phpmd:~2.2 sebastian/phpcpd:* \
    squizlabs/php_codesniffer:* mayflower/php-codebrowser:~1.1 codeception/codeception:*
#RUN echo "export PATH=$PATH:/home/jenkins/.composer/vendor/bin" >> $JENKINS_HOME/.bashrc # Keep dreaming!

USER root
RUN apt-get clean -y

# Go back to jenkins user.
USER jenkins
