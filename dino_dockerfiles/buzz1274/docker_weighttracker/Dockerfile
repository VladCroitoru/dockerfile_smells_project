# Version 0.0.1
FROM centos:6.6
MAINTAINER David Exelby "david@sulaco.co.uk"
RUN yum update -y
RUN yum install -y tar
RUN yum install -y wget
RUN yum groupinstall -y development
RUN yum install -y httpd

#configure php
RUN yum install -y php
RUN yum install -y php-devel
RUN yum install -y pcre-devel
RUN yum install -y php-pear
RUN yum install -y php-pgsql
RUN yum install -y php-pdo
RUN pear config-set php_ini /etc/php.ini
RUN rpm -Uvh https://mirror.webtatic.com/yum/el6/latest.rpm
RUN yum install -y yum-plugin-replace
RUN yum replace -y php-common --replace-with=php55w-common
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=bin --filename=composer

#install phalcon
WORKDIR /usr/local
RUN git clone git://github.com/phalcon/cphalcon.git
WORKDIR /usr/local/cphalcon/build
RUN ./install
RUN echo extension=phalcon.so >> /etc/php.d/phalcon.ini
WORKDIR /usr/local
RUN git clone https://github.com/phalcon/phalcon-devtools.git
RUN ln -s /usr/local/phalcon-devtools/phalcon.php /usr/bin/phalcon
RUN chmod ugo+x /usr/bin/phalcon

#install postgresql
RUN rpm -Uvh http://yum.postgresql.org/9.3/redhat/rhel-6-x86_64/pgdg-redhat93-9.3-1.noarch.rpm
RUN yum install -y postgresql93-devel.x86_64

#install node
WORKDIR /usr/local
RUN wget http://nodejs.org/dist/v0.12.2/node-v0.12.2.tar.gz
RUN tar -xzvf node-v0.12.2.tar.gz
RUN rm node-v0.12.2.tar.gz
WORKDIR /usr/local/node-v0.12.2
RUN ./configure && make && make install

#install bower
RUN npm install -g bower
RUN npm install -g bower-installer

#install phantomjs
RUN npm install -g phantomjs

#install ember-cli
RUN npm install -g ember-cli

#configure httpd.conf
RUN rm -rf /var/www/cgi-bin
RUN rm -rf /var/www/icons
RUN rm -rf /var/www/error
COPY weighttracker.zz50.co.uk.conf /etc/httpd/conf.d/weighttracker.zz50.co.uk.conf

WORKDIR /
ENTRYPOINT /usr/sbin/httpd -DFOREGROUND
EXPOSE 80
EXPOSE 443
