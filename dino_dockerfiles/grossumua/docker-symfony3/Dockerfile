FROM      ubuntu:14.04.4
MAINTAINER Olexander Kutsenko    <olexander.kutsenko@gmail.com>

#Create docker user
RUN mkdir -p /var/www
RUN mkdir -p /home/docker
RUN useradd -d /home/docker -s /bin/bash -M -N -G www-data,sudo,root docker
RUN echo docker:docker | chpasswd
RUN usermod -G www-data,users www-data
RUN chown -R docker:www-data /var/www
RUN chown -R docker:www-data /home/docker

#install Software
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y software-properties-common python-software-properties
RUN apt-get install -y git git-core vim nano mc nginx screen curl unzip wget
RUN apt-get install -y supervisor memcached htop tmux zip
COPY configs/supervisor/cron.conf /etc/supervisor/conf.d/cron.conf
COPY configs/nginx/default /etc/nginx/sites-available/default

#Install PHP
RUN apt-get install -y language-pack-en-base
RUN LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php
RUN apt-get update 
RUN apt-get install -y php7.0 php7.0-cli php7.0-common php7.0-cgi php7.0-curl php7.0-imap php7.0-pgsql
RUN apt-get install -y php7.0-sqlite3 php7.0-mysql php7.0-fpm php7.0-intl php7.0-gd php7.0-json
RUN apt-get install -y php-memcached php-memcache php-imagick php7.0-xml php7.0-mbstring php7.0-ctype
RUN apt-get install -y php7.0-dev php-pear
RUN pecl install xdebug
RUN rm /etc/php/7.0/cgi/php.ini
RUN rm /etc/php/7.0/cli/php.ini
RUN rm /etc/php/7.0/fpm/php.ini
RUN rm /etc/php/7.0/fpm/pool.d/www.conf
COPY configs/php/www.conf /etc/php/7.0/fpm/pool.d/www.conf
COPY configs/php/php.ini  /etc/php/7.0/cgi/php.ini
COPY configs/php/php.ini  /etc/php/7.0/cli/php.ini
COPY configs/php/php.ini  /etc/php/7.0/fpm/php.ini
COPY configs/php/xdebug.ini /etc/php/7.0/mods-available/xdebug.ini

#Install Percona Mysql 5.6 server
RUN wget https://repo.percona.com/apt/percona-release_0.1-3.$(lsb_release -sc)_all.deb
RUN dpkg -i percona-release_0.1-3.$(lsb_release -sc)_all.deb
RUN rm percona-release_0.1-3.$(lsb_release -sc)_all.deb
RUN apt-get update
RUN echo "percona-server-server-5.6 percona-server-server/root_password password root" | sudo debconf-set-selections
RUN echo "percona-server-server-5.6 percona-server-server/root_password_again password root" | sudo debconf-set-selections
RUN apt-get install -y percona-server-server-5.6
COPY configs/mysql/my.cnf /etc/mysql/my.cnf

# SSH service
RUN sudo apt-get install -y openssh-server openssh-client
RUN sudo mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
#change 'pass' to your secret password
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config
# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

#configs bash start
COPY configs/autostart.sh /root/autostart.sh
RUN  chmod +x /root/autostart.sh
COPY configs/bash.bashrc /etc/bash.bashrc
COPY configs/.bashrc /root/.bashrc
COPY configs/.bashrc /home/docker/.bashrc

#Install locale
RUN locale-gen en_US.UTF-8
RUN dpkg-reconfigure locales

#Install Java 8
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886
RUN add-apt-repository -y ppa:webupd8team/java
RUN apt-get update
# Accept license non-iteractive
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | sudo /usr/bin/debconf-set-selections
RUN apt-get install -y oracle-java8-installer
RUN apt-get install -y oracle-java8-set-default
RUN echo "JAVA_HOME=/usr/lib/jvm/java-8-oracle" | sudo tee -a /etc/environment
RUN export JAVA_HOME=/usr/lib/jvm/java-8-oracle

#ant install
RUN sudo apt-get install -y ant

#Autocomplete symfony3
COPY configs/files/symfony3-autocomplete.bash /etc/bash_completion.d/symfony3-autocomplete.bash

#Composer
RUN cd /home
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin/ --filename=composer
RUN chmod 777 /usr/local/bin/composer

#Code standart
RUN composer global require "squizlabs/php_codesniffer=*"
RUN composer global require "sebastian/phpcpd=*"
RUN composer global require "phpmd/phpmd=@stable"
RUN cd /usr/bin && ln -s ~/.composer/vendor/bin/phpcpd
RUN cd /usr/bin && ln -s ~/.composer/vendor/bin/phpmd
RUN cd /usr/bin && ln -s ~/.composer/vendor/bin/phpcs

#etcKeeper
RUN mkdir -p /root/etckeeper
COPY configs/etckeeper.sh /root/etckeeper.sh
COPY configs/files/etckeeper-hook.sh /root/etckeeper/etckeeper-hook.sh
RUN chmod +x /root/etckeeper/*.sh
RUN chmod +x /root/*.sh
RUN /root/etckeeper.sh

#open ports
EXPOSE 80 22 9000
