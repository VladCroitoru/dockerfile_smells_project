FROM             ubuntu:14.04
MAINTAINER       Nikos Maris

ENV REFRESHED_AT=2017-02-26 \
    #PROXY=http://proxy.example.ch:80 \
    DEBIAN_FRONTEND=noninteractive

RUN ifconfig eth0 | grep "inet addr" | cut -d ':' -f 2 | cut -d ' ' -f 1 > /host

RUN apt-get -qqy update && \
    dpkg-divert --local --rename --add /sbin/initctl && \
    ln -sf /bin/true /sbin/initctl && \
    apt-get -qy install curl

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -

# Additional base packages
RUN apt-get -qy install git vim-tiny wget pwgen \
  mysql-client mysql-server \
  apache2 libapache2-mod-php5 php5-mysql php5-gd php5-curl \
  python-setuptools \
  postfix \
  nodejs build-essential \
  netcat net-tools vim sshpass && \
  apt-get -q autoclean

# drush: instead of installing a package, pull via composer into /opt/composer
# http://www.whaaat.com/installing-drush-7-using-composer
RUN curl -sS https://getcomposer.org/installer | php && \
    mv composer.phar /usr/local/bin/composer && \
    COMPOSER_HOME=/opt/composer composer --quiet global require drush/drush:8.* && \
    ln -s /opt/composer/vendor/drush/drush/drush /bin/drush
# Add drush comand https://www.drupal.org/project/registry_rebuild
RUN wget http://ftp.drupal.org/files/projects/registry_rebuild-7.x-2.2.tar.gz && \
    tar xzf registry_rebuild-7.x-2.2.tar.gz && \
    rm registry_rebuild-7.x-2.2.tar.gz && \
    mv registry_rebuild /opt/composer/vendor/drush/drush/commands
#RUN sed -i '1i export PATH="$HOME/.composer/vendor/bin:$PATH"' /root/.bashrc
RUN /bin/drush --version
RUN /bin/drush dl drush_language-7.x

ADD files/root/.my.cnf.sample /root/.my.cnf.sample
RUN sed -i "s/localhost/$(cat /host)/" /root/.my.cnf.sample

# Sample backup script
ADD files/backup.sh  /root/backup.sh
# Webfactory specifc
ADD files/webfact_rm_site.sh /tmp/.webfact_rm_site.sh

ARG VIRTUAL_HOST=drupal
  # Make sure we have a proper working terminal
ARG TERM=xterm
  ## Drupal settings: used by start.sh within the container
  #  can be overridden at run time e.g. -e "DRUPAL_XX=YY"
ARG DRUPAL_DOCROOT=/var/www/html
  # D) Pull The entire Drupal site from a Repo, default is master branch
  #DRUPAL_GIT_REPO=https://USER:PASSWORD@example.org/path/something
ARG DRUPAL_GIT_BRANCH=master
  #DRUPAL_INSTALL_REPO=https://github.com/Boran/drupal-profile1.git
ARG DRUPAL_INSTALL_PROFILE=standard
ARG DRUPAL_INSTALL_PROFILE_BRANCH=master
  # During build test: copy in directly
  #ADD ./drupal-profile1      /var/www/html/profiles/boran1

  ### Run a feature revert revert after installing, can be useful for default content
  #DRUPAL_MAKE_FEATURE_REVERT=1

  ## Default Drupal settings
ARG DRUPAL_SITE_NAME="My Drupal Site"
ARG DRUPAL_SITE_EMAIL=drupal@example.ch
ARG DRUPAL_ADMIN=admin
ARG DRUPAL_ADMIN_PW=admin
ARG DRUPAL_ADMIN_EMAIL=root@example.ch
  #by default no second user  
  #DRUPAL_USER1=admin2 DRUPAL_USER1_PW=admin2 DRUPAL_USER1_EMAIL=drupal@example.ch ENV DRUPAL_USER1_ROLE=administrator

  # Run a custom command after the site is installed
  # Example: get, enable and run the production check module
  #DRUPAL_FINAL_CMD="drush -y dl prod_check && drush -y en prod_check && drush -y cache-clear drush && drush -y prod-check-prodmode"
# /ARG

# Setup a default postfix to allow local delivery and stop drupal complaining
#  for external delivery add local config to custom.sh such as:
#  postconf -e 'relayhost = myrelay.example.ch'
ADD ./files/postfix.sh /opt/postfix.sh
RUN chmod 755 /opt/postfix.sh

### Custom startup scripts
RUN easy_install supervisor

# Retrieve drupal: changed - now in start.sh to allow for makes too.
# Push down a copy of drupal
#ADD ./files/drupal-7  /tmp/drupal

ADD ./files/webfact_status.sh /tmp/webfact_status.sh
ADD ./files/supervisord.conf /etc/supervisord.conf
ADD ./files/supervisord.d    /etc/supervisord.d
ADD ./files/init.d/*         /etc/init.d/
ADD ./files/foreground.sh    /etc/apache2/foreground.sh
ADD ./ubuntu1404/000-default.conf /etc/apache2/sites-available/000-default.conf
ADD ./ubuntu1404/default-ssl.conf /etc/apache2/sites-available/default-ssl.conf
ADD ./start.sh /start.sh

#VOLUME ["/var/www/html", "/data"]
# Using /var/www/html as WORKDIR causes docker exec to fail in certain cases
#WORKDIR /var/www/html
WORKDIR /var
# Automate starting of mysql+apache, allow bash for debugging
RUN chmod 755 /start.sh /etc/apache2/foreground.sh
EXPOSE 80 9999

RUN mkdir -p /opt/install
RUN mkdir -p /opt/module/test
RUN mkdir -p /opt/drush-make

COPY install/ /opt/install/
RUN ls -la /opt/install
RUN cp /opt/install/drupal.make /opt/drush-make/drupal.make || bash -c "echo 'missing install/drupal.make' && exit 1"
RUN cp /opt/install/custom.sh /opt/drush-make/custom.sh || echo 'skipping composer due to missing install/custom.sh'
COPY wait-for-port.sh /wait-for-port.sh
COPY log.sh /log.sh

RUN chmod 777 /wait-for-port.sh
RUN chmod 777 /log.sh
###################################################################
RUN cd /var && bash /start.sh
# while installing drupal in the background, in parallel we are installing packaging at the following of tests
RUN bash -c "cp /opt/install/package.json /opt/module/test/package.json && cd /opt/module/test && npm install && cd -" || echo "skipping nodejs due to missing install/package.json"

RUN cd / && ifconfig && ./wait-for-port.sh 80 300 && sleep 20
# commented the following as its error can be ignored
# && supervisorctl status
##################################################################
# so that the entrypoint (overwritten by the command at the docker-compose yml file) can start supervisord in the foreground
RUN supervisorctl stop httpd postfix mysqld

CMD ["supervisord", "-c", "/etc/supervisord.conf", "-n"]
HEALTHCHECK CMD curl -f http://$(cat /host) || exit 1

