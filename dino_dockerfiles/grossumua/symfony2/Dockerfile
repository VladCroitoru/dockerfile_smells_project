FROM      ubuntu:14.04.4
MAINTAINER Olexander Kutsenko <olexander.kutsenko@gmail.com>

#Create docker user
RUN mkdir -p /home/docker
RUN useradd -d /home/docker -s /bin/bash -M -N -G www-data,sudo,root docker
RUN chown -R docker:www-data /home/docker
RUN echo docker:docker | chpasswd
RUN usermod -G www-data,users www-data

#install PHP
RUN apt-get update
RUN apt-get install -y software-properties-common python-software-properties
RUN apt-get install -y git git-core vim nano mc nginx screen curl unzip
RUN apt-get install -y wget php5 php5-fpm php5-cli php5-common php5-intl 
RUN apt-get install -y php5-json php5-mysql php5-gd php5-imagick
RUN apt-get install -y php5-curl php5-mcrypt php5-dev php5-xdebug
COPY configs/php5-fpm/php.ini /etc/php5/fpm/php.ini
COPY configs/php5-fpm/www.conf /etc/php5/fpm/pool.d/www.conf
COPY configs/nginx/default /etc/nginx/sites-available/default
COPY configs/php5-fpm/xdebug.ini /etc/php5/mods-available/xdebug.ini

#MySQL install + password
RUN echo "mysql-server mysql-server/root_password password root" | debconf-set-selections
RUN echo "mysql-server mysql-server/root_password_again password root" | debconf-set-selections
RUN sudo apt-get  install -y mysql-server mysql-client

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
RUN chmod +x /root/autostart.sh
COPY configs/bash.bashrc /etc/bash.bashrc

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

#Autocomplete symfony2
COPY configs/files/symfony2-autocomplete.bash /etc/bash_completion.d/symfony2-autocomplete.bash
COPY configs/.bashrc /root/.bashrc
COPY configs/.bashrc /home/docker/.bashrc

#etcKeeper
RUN mkdir -p /root/etckeeper
COPY configs/etckeeper.sh /root/etckeeper.sh
COPY configs/files/etckeeper-hook.sh /root/etckeeper/etckeeper-hook.sh
RUN /root/etckeeper.sh

#open ports
EXPOSE 80 22 9000
