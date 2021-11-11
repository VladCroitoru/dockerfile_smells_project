# The MIT License
#
#  Copyright (c) 2015, CloudBees, Inc.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.

FROM jenkinsci/slave
MAINTAINER Julien 'Lta' BALLET <contact@lta.io>

#
# Install a bunch of web development related packages
# As well as sudo to allow to hack the image in jenkins
#
USER root

# Getting recent php versions
COPY dotdeb.list /etc/apt/sources.list.d/dotdeb.list
RUN wget -O- https://www.dotdeb.org/dotdeb.gpg | apt-key add -

# Get a recent version of MySQL
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys 5072E1F5
COPY mysql.list /etc/apt/sources.list.d/mysql.list

# Getting recent node version
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -

# Avoid ERROR: invoke-rc.d: policy-rc.d denied execution of start.
RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d

# Got up-to-date shit :)
RUN apt-get update -y
RUN apt-get dist-upgrade -y

# Configure Mysql
RUN echo 'mysql-community-server mysql-community-server/root-pass password root' | debconf-set-selections
RUN echo 'mysql-community-server mysql-community-server/re-root-pass password root' | debconf-set-selections

RUN apt-get install -qy \
    curl s3cmd \
    build-essential \
    ruby ruby-dev \
    nodejs \
    mysql-community-server \
    redis-server \
    elasticsearch \
    sudo

RUN service mysql stop
RUN service redis-server stop
RUN service elasticsearch stop

# All the PHP bullshit
RUN apt-get install -qy \
    php7.0-cli php7.0-dev \
    php7.0-curl php7.0-gd php7.0-json php7.0-mbstring php7.0-opcache \
    php7.0-readline php7.0-soap php7.0-bcmath php7.0-bz2 php7.0-cgi php7.0-dba \
    php7.0-enchant php7.0-fpm php7.0-geoip php7.0-gmp php7.0-igbinary \
    php7.0-imagick php7.0-imap php7.0-interbase php7.0-intl php7.0-ldap \
    php7.0-mcrypt php7.0-memcached php7.0-mongodb php7.0-msgpack php7.0-mysql \
    php7.0-odbc php7.0-pgsql php7.0-phpdbg php7.0-pspell php7.0-recode \
    php7.0-redis php7.0-sqlite3 php7.0-ssh2 php7.0-sybase \
    php7.0-tidy php7.0-xmlrpc php7.0-xsl php7.0-zip

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

COPY jenkins.sudoers /etc/sudoers.d/jenkins

COPY jenkins-slave /usr/local/bin/jenkins-slave

USER jenkins
ENTRYPOINT ["jenkins-slave"]
