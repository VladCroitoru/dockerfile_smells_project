FROM centos:6

MAINTAINER Battcor <battcor@gmail.com>

WORKDIR /tmp

RUN yum -y install epel-release wget gcc && \
    wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm && \
    wget https://centos6.iuscommunity.org/ius-release.rpm && \
    rpm -Uvh ius-release*.rpm && \
    yum -y update

RUN echo -e "[mariadb]" >> /etc/yum.repos.d/MariaDB.repo && \
    echo -e "name = MariaDB" >> /etc/yum.repos.d/MariaDB.repo && \
    echo -e "baseurl = http://yum.mariadb.org/10.1/centos6-amd64" >> /etc/yum.repos.d/MariaDB.repo && \
    echo -e "gpgkey = https://yum.mariadb.org/RPM-GPG-KEY-MariaDB" >> /etc/yum.repos.d/MariaDB.repo && \
    echo -e "gpgcheck=1" >> /etc/yum.repos.d/MariaDB.repo

RUN yum -y install php56u-fpm php56u php56u-opcache php56u-xml php56u-mcrypt php56u-gd php56u-devel php56u-mysql php56u-intl php56u-mbstring php56u-bcmath php56u-pecl-memcache \
    git MariaDB-client MariaDB-server nginx supervisor unzip

RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip" && \
    unzip awscli-bundle.zip && \
    ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer

RUN git clone git://github.com/phalcon/cphalcon.git && \
    cd cphalcon/ && \
    git checkout tags/v3.2.2 && \
    cd build && \
    ./install && \
    echo -e "extension=phalcon.so" > /etc/php.d/phalcon.ini

RUN chkconfig supervisord on && \
    echo -e "short_open_tag=On" > /etc/php.d/shortopentags.ini && \
    echo -e "date.timezone=\"America/New_York\"" > /etc/php.d/timezone.ini

WORKDIR /var/www/html

CMD ["sh", "start.sh"]

EXPOSE 80
EXPOSE 443
