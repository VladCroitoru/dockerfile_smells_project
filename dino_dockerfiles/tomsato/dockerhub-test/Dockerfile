FROM centos:6

MAINTAINER tomsato

# yumが遅いので一旦fastestmirrorを無効にする
RUN sed -i 's/enabled=1/enabled=0/' /etc/yum/pluginconf.d/fastestmirror.conf

RUN yum -y update

# util
RUN yum -y install wget vim git tar

# PHP
RUN yum -y install epel-release
RUN rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm
RUN yum -y install --enablerepo=remi,remi-php56 php php-devel php-mbstring php-pdo php-gd php-xml

# httpd
RUN wget -O /etc/yum.repos.d/epel-httpd24.repo http://repos.fedorapeople.org/repos/jkaluza/httpd24/epel-httpd24.repo
RUN yum -y install --enablerepo=epel-httpd24 httpd24
RUN ln -s /opt/rh/httpd24/root/etc/httpd     /etc/httpd24
RUN ln -s /opt/rh/httpd24/root/var/www/html  /var/www/html24
RUN ln -s /opt/rh/httpd24/root/var/log/httpd /var/log/httpd24
ADD src/index.html /var/www/html24/
RUN sed -i 's/#ServerName www.example.com:80/ServerName www.example.com:80/' /etc/httpd24/conf/httpd.conf
RUN yum -y remove httpd

# # MySQL
# RUN yum -y install http://dev.mysql.com/get/mysql-community-release-el6-5.noarch.rpm
# RUN yum -y install mysql-community-server
# RUN mysql_install_db --datadir=/var/lib/mysql --user=mysql

# dev tool
RUN yum -y groupinstall "Development tools"
RUN yum -y install source-highlight

# ssh
RUN yum -y install passwd openssh openssh-server openssh-clients sudo
RUN mkdir -p /var/run/sshd
RUN useradd -d /home/tomsato -m -s /bin/bash tomsato
RUN echo tomsato:tomsato | chpasswd
RUN echo 'tomsato ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
ADD sshd/sshd_config /etc/ssh/sshd_config
RUN /etc/init.d/sshd start;/etc/init.d/sshd stop

# dotfile
COPY dotfiles/bashrc    /etc/bashrc
COPY dotfiles/vimrc     /home/tomsato/.vimrc
COPY dotfiles/gitconfig /home/tomsato/.gitconfig
RUN chown tomsato:users /home/tomsato/.vimrc
RUN chown tomsato:users /home/tomsato/.gitconfig

# supervisor
RUN yum -y install python-setuptools
RUN easy_install 'supervisor == 3.2.0' 'supervisor-stdout == 0.1.1' && mkdir -p /var/log/supervisor
ADD conf/supervisord.conf /etc/supervisord.conf

# expose for sshd, httpd, mysql
EXPOSE 22 80 3306

CMD ["/usr/bin/supervisord"]
