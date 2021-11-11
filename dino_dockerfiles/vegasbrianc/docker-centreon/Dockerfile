FROM ubuntu:precise
MAINTAINER Philipp Adelt <info@philipp.adelt.net>
RUN apt-get update
RUN apt-get -y upgrade
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install apt-utils
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python2.7 libperl-dev mysql-client apache2 libapache2-mod-php5 python-setuptools nano mc vim-tiny php5-memcached php5-geoip php5-gd php5-ldap php5-imap php5-pgsql php5-mcrypt sudo heirloom-mailx lsb-release build-essential apache2 apache2-mpm-prefork php5 php5-mysql php-pear php5-ldap php5-snmp php5-gd mysql-server libmysqlclient-dev rrdtool librrds-perl libconfig-inifiles-perl libcrypt-des-perl libdigest-hmac-perl libdigest-sha-perl libgd-gd2-perl snmp snmpd libnet-snmp-perl libsnmp-perl libgd2-xpm libgd2-xpm-dev libpng12-dev postfix wget iputils-ping smbclient libssl-dev dnsutils fping less vim net-tools rsyslog supervisor

ADD files/bashrc /.bashrc

# Install Nagios 3
# Nagios installation information from http://nagios.sourceforge.net/docs/3_0/quickstart-ubuntu.html
# NDOutils, Centreon etc. from http://en.doc.centreon.com/Docs:Centreon2

RUN useradd -m -s /bin/bash nagios
RUN bash -c "echo nagios:nagios | chpasswd"
RUN groupadd nagcmd
RUN usermod -a -G nagcmd nagios
RUN usermod -a -G nagcmd www-data
RUN mkdir /root/nagios
WORKDIR /root/nagios
ADD http://prdownloads.sourceforge.net/sourceforge/nagios/nagios-3.5.1.tar.gz /root/nagios/
RUN tar -xzvf nagios-3.5.1.tar.gz

ADD http://nagios-plugins.org/download/nagios-plugins-2.0.3.tar.gz /root/nagios/
RUN tar -xzf nagios-plugins-2.0.3.tar.gz

ADD http://downloads.sourceforge.net/project/nagios/ndoutils-1.x/ndoutils-1.5.2/ndoutils-1.5.2.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fnagios%2Ffiles%2Fndoutils-1.x%2Fndoutils-1.5.2%2F&ts=1407940576&use_mirror=kent /root/nagios/
RUN tar -xzf ndoutils-1.5.2.tar.gz

ADD http://download.centreon.com/centreon/centreon-2.5.2.tar.gz /root/nagios/
RUN tar -xzf centreon-2.5.2.tar.gz
RUN chown -R root:root centreon-2.5.2

# Build Nagios
WORKDIR /root/nagios/nagios
RUN ./configure --with-command-group=nagcmd --enable-nanosleep --enable-event-broker --enable-embedded-perl --prefix=/usr/local/nagios 2>&1 | tail -n 10
RUN make all  2>&1 | tail -n 10
RUN make install
RUN make install-commandmode
RUN make install-init
VOLUME /usr/local/nagios/etc
VOLUME /usr/local/nagios/var
RUN chgrp nagios /usr/local/nagios/etc/
RUN chmod g+w /usr/local/nagios/etc/
# Initially add some configs
ADD files/nagios-init.cfg /root/nagios/nagios.cfg
ADD files/initialize.sh /root/nagios/initialize.sh
RUN chmod +x /root/nagios/initialize.sh
ADD files/restart-nagios.sh /restart-nagios.sh
RUN chmod +x /restart-nagios.sh
RUN cp p1.pl /usr/local/nagios/share/

RUN mkdir -p /var/log/nagios/rw
RUN chown -R nagios:nagios /var/log/nagios
RUN chmod -R 775 /var/log/nagios

#Lets edit our MySQL File
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = localhost/" /etc/mysql/my.cnf
RUN sed -i -e"s/^key_buffer\s*=\s*16M/key_buffer_size = 16M/" /etc/mysql/my.cnf
RUN sed -i -e"s/^user\s*=\s*mysql/user = root/" /etc/mysql/my.cnf

# Now for the plugins
WORKDIR /root/nagios/nagios-plugins-2.0.3
RUN ./configure --with-nagios-user=nagios --with-nagios-group=nagios  2>&1 | tail -n 10
# The DEBUG_NDO2DB flag (only) makes ndo2db non-daemonize itself, which is necessary for supervisord.
RUN make 2>&1 | tail -n 10
RUN make install

# NDOUtils
WORKDIR /root/nagios/ndoutils-1.5.2
RUN bash -c "CFLAGS=-DDEBUG_NDO2DB ./configure --prefix=/usr/local/nagios/ --enable-mysql --disable-pgsql --with-ndo2db-user=nagios --with-ndo2db-group=nagios 2>&1 | tail -n 10"
RUN make 2>&1 | tail -n 10
RUN cp src/ndomod-3x.o /usr/local/nagios/bin/ndomod.o
RUN cp src/ndo2db-3x /usr/local/nagios/bin/ndo2db
RUN cp src/log2ndo /usr/local/nagios/bin/
RUN cp src/file2sock /usr/local/nagios/bin/
RUN chmod 774 /usr/local/nagios/bin/ndo*
RUN chown nagios:nagios /usr/local/nagios/bin/ndo*

# Centreon itself
WORKDIR /root/nagios/centreon-2.5.2/
ADD files/centreon-silent-install.txt /root/nagios/centreon-silent-install.txt
RUN useradd -m centreon
RUN touch /etc/init.d/nagios
RUN ./install.sh -f ../centreon-silent-install.txt
RUN adduser centreon www-data
# move files aside so that start.sh can copy them to volume centreon-etc
RUN mv /etc/centreon /root/centreon-etc

# http://museum.php.net/php5/php-5.3.1.tar.bz2
ADD files/start.sh /start.sh
ADD files/foreground.sh /etc/apache2/foreground.sh
ADD files/supervisord.conf /etc/supervisord.conf
RUN chmod 755 /start.sh
RUN chmod 755 /etc/apache2/foreground.sh
EXPOSE 80
CMD ["/bin/bash", "/start.sh"]
