FROM    ubuntu:precise
MAINTAINER Andreas Jansson andreas@jansson.me.uk

RUN     echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN     apt-get update
RUN     apt-get -y install \
            apache2 \
            php5 \
            php5-mysql \
            php5-dev \
            mysql-server \
            curl \
            graphviz \
            supervisor \
            openssh-server \
            build-essential \
            python-pip

# download and build the extension
RUN     curl -L https://github.com/preinheimer/xhprof/tarball/3bbf52e | tar xz && \
            mv preinheimer-xhprof-3bbf52e /opt/xhprof && \
            cd /opt/xhprof/extension && \
            phpize && \
            ./configure --with-php-config=/usr/bin/php-config && \
            make && \
            make install

# add some confs
ADD     xhprof_vhost.conf.tpl /etc/apache2/sites-enabled/
ADD     config.php.tpl /opt/xhprof/xhprof_lib/
RUN     rm /etc/apache2/sites-enabled/000-default

ADD     my.cnf /etc/mysql/
ADD     schema.sql /tmp/

# setup sshd with root:root
RUN	mkdir /var/run/sshd
RUN     echo 'root:root' | chpasswd

ADD     supervisord.conf /etc/supervisor/supervisord.conf

RUN     pip install envtpl==0.2.1

ADD     start.sh /bin/
RUN     chmod +x /bin/start.sh

EXPOSE  3306 22 80

CMD     /bin/start.sh
