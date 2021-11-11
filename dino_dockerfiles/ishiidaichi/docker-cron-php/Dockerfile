FROM centos:centos6

MAINTAINER ishiidaichi

RUN yum -y update

RUN yum -y install passwd sudo gcc-c++ vim gcc make git mysql mysql-client python-setuptools mercurial
RUN yum -y install openssh openssl-devel zlib-devel readline-devel sqlite-devel bzip2-devel libevent-devel
RUN yum -y install openssh-server openssh-clients python-setuptools wget tar libxslt-devel libxml2-devel python-dev
RUN yum -y install python-devel bzip2-devel expat-devel gdbm-devel readline-devel mysql-devel scipy numpy

RUN rpm -Uvh http://ftp.iij.ad.jp/pub/linux/fedora/epel/6/x86_64/epel-release-6-8.noarch.rpm
RUN rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm
RUN yum -y install --enablerepo=epel -y mosh
RUN yum -y install gd-last --enablerepo=remi
RUN yum -y install --enablerepo=remi --enablerepo=remi-php56 php php-opcache php-devel php-mbstring php-mcrypt php-mysqlnd php-pecl-xdebug php-pecl-xhprof pcre-devel php-gd

ADD mongodb.repo /etc/yum.repos.d/mongodb.repo
RUN yum install -y mongodb-org-shell mongodb-org-tools
RUN pecl install mongo
RUN echo extension=mongo.so >> /etc/php.d/mongo.ini

RUN git clone --depth=1 git://github.com/phalcon/cphalcon.git /root/phalcon
RUN cd /root/phalcon/build && ./install 64bits
RUN echo extension=/usr/lib64/php/modules/phalcon.so >> /etc/php.d/phalcon.ini

RUN wget http://www.python.org/ftp/python/2.7.9/Python-2.7.9.tgz && \
tar xzvf Python-2.7.9.tgz && \
cd Python-2.7.9 && \
./configure --enable-shared --with-threads --enable-unicode=ucs4 --prefix=/usr/local && \
make && \
make altinstall && \
cd ..
RUN rm -rf Python-2.7.9.tgz
RUN rm -rf Python-2.7.9
RUN ln -s /usr/local/bin/python2.7 /usr/local/bin/python
RUN ln -s /usr/local/lib/libpython2.7.so /usr/lib
RUN ln -s /usr/local/lib/libpython2.7.so.1.0 /usr/lib
RUN /sbin/ldconfig -v

RUN wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
RUN python ez_setup.py
RUN easy_install pip
RUN pip install -e hg+https://bitbucket.org/dbenamy/devcron#egg=devcron

VOLUME ["/cron"]

CMD ["devcron.py", "/cron/crontab"]
