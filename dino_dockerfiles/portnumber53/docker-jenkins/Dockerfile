FROM archlinux/base:latest

RUN pacman -Syu --noconfirm jdk8-openjdk \
  && pacman --noconfirm -Scc

RUN archlinux-java set java-8-openjdk

RUN pacman -Syu --noconfirm \
    base-devel \
    lftp \
    php \
    php-gd \
    php-pgsql \
    xdebug \
    php-imap \
    php-sqlite \
    php-xsl \
    apache-ant \
    rsync \
    binutils \
    fakeroot \
    unzip \
    ttf-dejavu \
    git \
    openssh \
    mysql \
    nodejs \
    npm \
  && pacman --noconfirm -Scc

RUN curl -OL https://phar.phpunit.de/phpunit-6.phar \
    && chmod +x phpunit-6.phar \
    && mv phpunit-6.phar /usr/local/bin/phpunit

RUN curl -OL https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar \
    && chmod +x phpcs.phar \
    && mv phpcs.phar /usr/local/bin/phpcs

RUN curl -OL https://squizlabs.github.io/PHP_CodeSniffer/phpcbf.phar \
    && chmod +x phpcbf.phar \
    && mv phpcbf.phar /usr/local/bin/phpcbf

RUN curl -OL https://phar.phpunit.de/phploc.phar \
    && chmod +x phploc.phar \
    && mv phploc.phar /usr/local/bin/phploc

RUN curl -OL http://static.pdepend.org/php/latest/pdepend.phar \
    && chmod +x pdepend.phar \
    && mv pdepend.phar /usr/local/bin/pdepend

RUN curl -OL http://static.phpmd.org/php/latest/phpmd.phar \
    && chmod +x phpmd.phar \
    && mv phpmd.phar /usr/local/bin/phpmd

RUN curl -OL https://phar.phpunit.de/phpcpd.phar \
    && chmod +x phpcpd.phar \
    && mv phpcpd.phar /usr/local/bin/phpcpd

RUN curl -OL http://phpdox.de/releases/phpdox.phar \
    && chmod +x phpdox.phar \
    && mv phpdox.phar /usr/local/bin/phpdox

RUN curl -OL https://getcomposer.org/composer.phar \
    && chmod +x composer.phar \
    && mv composer.phar /usr/local/bin/composer

# Install Codeception
RUN curl -o codecept.phar http://codeception.com/codecept.phar \
    && chmod +x codecept.phar \
    && mv codecept.phar /usr/local/bin/codecept

RUN npm install -g yo grunt-cli bower express

# Angular CLI ( https://github.com/nodejs/node-gyp/issues/454 )
RUN npm install -g node-gyp \
    && npm install --unsafe-perm -g @angular/cli@latest

# Bower
RUN npm install bower -g

# Gulp
RUN npm install gulp-cli -g
RUN npm install gulp -g

# `/usr/share/jenkins/ref/` contains all reference configuration we want
# to set on a fresh new installation. Use it to bundle additional plugins
# or config file with your custom jenkins Docker image.
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d


ENV JENKINS_UC https://updates.jenkins.io
RUN chown -R ${user} "$JENKINS_HOME" /usr/share/jenkins/ref






ENV JENKINS_HOME /var/jenkins_home
ENV JENKINS_SLAVE_AGENT_PORT 50000

ARG user=jenkins
ARG group=jenkins
ARG uid=1000
ARG gid=1000

# Jenkins is run with user `jenkins`, uid = 1000
# If you bind mount a volume from the host or a data container,
# ensure you use the same uid
RUN groupadd -g ${gid} ${group} \
    && useradd -d "$JENKINS_HOME" -u ${uid} -g ${gid} -m -s /bin/bash ${user}

ENV TINI_VERSION 0.14.0
ENV TINI_SHA 6c41ec7d33e857d4779f14d9c74924cab0c7973485d2972419a3b7c7620ff5fd

# Use tini as subreaper in Docker container to adopt zombie processes 
RUN curl -fsSL https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini-static-amd64 -o \
    /bin/tini && chmod +x /bin/tini \
    && echo "$TINI_SHA  /bin/tini" | sha256sum -c -

COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/tcp-slave-agent-port.groovy

# jenkins version being bundled in this docker image
ARG JENKINS_VERSION
ENV JENKINS_VERSION ${JENKINS_VERSION:-2.168}

# jenkins.war checksum, download will be validated using it
ARG JENKINS_SHA=83756847b09e754829aaf343d2f11a8c84b097e922d1770dc53b8c8267184e62

# Can be used to customize where jenkins.war get downloaded from
ARG JENKINS_URL=https://repo.jenkins-ci.org/public/org/jenkins-ci/main/jenkins-war/${JENKINS_VERSION}/jenkins-war-${JENKINS_VERSION}.war

# could use ADD but this one does not check Last-Modified header neither does it allow to control checksum 
# see https://github.com/docker/docker/issues/8331
RUN curl -fsSL ${JENKINS_URL} -o /usr/share/jenkins/jenkins.war \
  && echo "${JENKINS_SHA}  /usr/share/jenkins/jenkins.war" | sha256sum -c -



ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log

COPY jenkins-support /usr/local/bin/jenkins-support
COPY jenkins.sh /usr/local/bin/jenkins.sh
ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins.sh"]

# from a derived Dockerfile, can use `RUN plugins.sh active.txt` to setup /usr/share/jenkins/ref/plugins from a support bundle
COPY plugins.sh /usr/local/bin/plugins.sh
COPY install-plugins.sh /usr/local/bin/install-plugins.sh




RUN install-plugins.sh \
        ansicolor \
        checkstyle \
        cloverphp \
        crap4j \
        dry \
        htmlpublisher \
        jdepend \
        plot \
        pmd \
        violations \
        warnings \
        xunit \
        shared-workspace \
        bitbucket \
        build-timestamp \
        workflow-aggregator


COPY enable-php-extension.sh /usr/local/bin/enable-php-extension.sh
RUN enable-php-extension.sh

RUN gpg --recv-key 72A321BAC245F175

RUN chown -Rv ${user}:${group} ${JENKINS_HOME} | tee
USER ${user}

RUN ls -la ${JENKINS_HOME} | tee \
  && mkdir -p ${JENKINS_HOME}/.gnupg  \
  && ls -la /var/jenkins_home/.gnupg

RUN gpg --recv-key 72A321BAC245F175

RUN cd /tmp && curl -o /tmp/php-pear.tar.gz https://aur.archlinux.org/cgit/aur.git/snapshot/php-pear.tar.gz \
  && tar -xvzf /tmp/php-pear.tar.gz \
  && rm /tmp/php-pear.tar.gz && cd php-pear/ \
  && sed -i 's#rm -rf ${pkgdir}/usr/share/pear/.{channels,depdb,depdblock,filemap,lock,registry}#rm -rf ${pkgdir}/.{channels,depdb,depdblock,filemap,lock,registry}#g' PKGBUILD \
  && makepkg \
  && mv /tmp/php-pear/php-pear-1\:1.10.12-2-any.pkg.tar.xz /tmp/php-pear-any.pkg.tar.xz \
  && rm -rf /tmp/php-pear/

USER root
RUN pacman -U --noconfirm /tmp/php-pear-any.pkg.tar.xz && rm /tmp/php-pear-any.pkg.tar.xz

RUN pecl install mongodb
RUN echo "extension=mongodb.so" >> `php --ini | grep "Loaded Configuration" | sed -e "s|.*:\s*||"`

USER ${user}



# for main web interface:
EXPOSE 8080

# will be used by attached slave agents:
EXPOSE 50000

# Jenkins home directory is a volume, so configuration and build history
# can be persisted and survive image upgrades
# Moved to the end per this SO: https://stackoverflow.com/questions/26145351/why-doesnt-chown-work-in-dockerfile
VOLUME /var/jenkins_home

