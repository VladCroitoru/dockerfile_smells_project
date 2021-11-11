FROM ubuntu:16.04
MAINTAINER Jean-Daniel Gasser <jean-daniel.gasser@altran.com>

# Update sources
RUN apt-get update -y

# install http
RUN apt-get install -y apache2 vim bash-completion unzip
RUN mkdir -p /var/lock/apache2 /var/run/apache2

# install mysql
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-client mysql-server

# install MongoDB
RUN mkdir -p /data/db
RUN apt-get install -y mongodb mongodb-server mongodb-clients

# install php
RUN apt-get install -y php7.0 php7.0-mysql libapache2-mod-php7.0 

#Install curl
RUN apt-get install -y curl

#install sudo
RUN apt-get install -y sudo

#install net-tools (netstat/ifconfig etc)
RUN apt-get install -y net-tools

# install nodejs 8.9.4 (dernière stable en 8.x)

RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo bash -
RUN apt-get install -y nodejs

# install git
RUN apt-get install -y git

# install sshd
RUN apt-get install -y openssh-server openssh-client passwd
RUN mkdir -p /var/run/sshd
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN echo 'root:root' | chpasswd

# Put your own public key at id_rsa.pub for key-based login.
RUN mkdir -p /root/.ssh && touch /root/.ssh/known_hosts && chmod 700 /root/.ssh
ADD known_hosts /root/.ssh/known_hosts

#install le nécessaire pour le déploiement continu sous rancher
RUN apt-get install -y python-setuptools
ADD rancher/ /rancher-gitlab-deploy
WORKDIR /rancher-gitlab-deploy
RUN python /rancher-gitlab-deploy/setup.py install
RUN ln -s /usr/local/bin/rancher-gitlab-deploy /usr/local/bin/upgrade

#install phpmyadmin
RUN apt-get install -y dbconfig-common dbconfig-mysql fontconfig-config fonts-dejavu-core javascript-common libfontconfig1 libfreetype6 libgd3 libjbig0 libjpeg-turbo8 libjpeg8 libjs-jquery libjs-sphinxdoc libjs-underscore libmcrypt4 libpng12-0 libtiff5 libvpx3 libxpm4 libxslt1.1 php-gd php-gettext php-mbstring php-mcrypt php-pear php-phpseclib php-tcpdf php-xml php7.0-gd php7.0-mbstring php7.0-mcrypt php7.0-xml

#Divers
ADD script.sh /root/
ADD key_rsa /root/
ADD version.txt /root/
ADD vhost_backend.conf /etc/apache2/sites-available/
ADD .bashrc /root/
EXPOSE 22 80 8080 3306

#pour démarer les services et concerver le containeur ouvert
CMD service mysql start && service apache2 start && service mongodb start && /usr/sbin/sshd -D
