FROM debian:9
MAINTAINER Jose A Alferez <correo@alferez.es>

ENV NAGIOS_VERSION 4.3.1
ENV DEBIAN_FRONTEND noninteractive

#### Configure TimeZone
RUN echo "Europe/Madrid" > /etc/timezone
RUN dpkg-reconfigure tzdata

#### Instalamos dependencias, Repositorios y Paquetes
RUN echo "deb http://httpredir.debian.org/debian stretch-backports main" >> /etc/apt/sources.list
RUN apt-get update -y --fix-missing
RUN apt-get -y upgrade

RUN apt-get install -y --fix-missing wget curl nano apache2 php-mysql build-essential php-cgi php-gd php-common php-curl libgd2-xpm-dev openssl libssl-dev xinetd apache2-utils unzip libapache2-mod-php php-cli  make mosquitto-clients bc dnsutils

#### Creamos el usuario
RUN groupadd nagios
RUN groupadd nagcmd
RUN useradd -u 3000 -g nagios -G nagcmd -d /usr/local/nagios -c 'Nagios Admin' nagios
RUN usermod -a -G nagcmd nagios
RUN usermod -G nagcmd www-data


### Instalamos Nagios
WORKDIR /tmp

COPY ./nagioscore /tmp/nagioscore

WORKDIR /tmp/nagioscore
RUN ./configure  --prefix=/usr/local/nagios --with-nagios-user=nagios --with-nagios-group=nagios --with-command-user=nagios --with-command-group=nagcmd
RUN make all
RUN make install
RUN make install-commandmode
RUN make install-init
RUN make install-config


RUN /usr/bin/install -c -m 644 sample-config/httpd.conf /etc/apache2/sites-available/nagios.conf

WORKDIR /tmp
RUN rm -rf nagios

RUN apt-get install -y --fix-missing  m4 gettext automake autoconf

### Instalamos los Plugins
#WORKDIR /tmp
COPY ./nagios-plugins /tmp/nagios-plugins
WORKDIR /tmp/nagios-plugins
RUN ./tools/setup
RUN ./configure --with-nagios-user=nagios --with-nagios-group=nagios --with-openssl
RUN make
RUN make install
RUN make install-root

WORKDIR /tmp
RUN rm -rf nagios-plugins



### Instalamos NRPE
WORKDIR /tmp
COPY ./nrpe /tmp/nrpe

WORKDIR /tmp/nrpe
RUN ./configure --enable-command-args --with-nagios-user=nagios --with-nagios-group=nagios --with-ssl=/usr/bin/openssl --with-ssl-lib=/usr/lib/x86_64-linux-gnu
RUN make all
RUN make install

WORKDIR /tmp
RUN rm -rf nrpe

#### Configuramos Apache
RUN a2enmod rewrite
RUN a2enmod cgi
RUN a2enmod auth_form
RUN a2enmod session_cookie
RUN a2enmod session_crypto
RUN a2enmod request
RUN echo "ServerName localhost" | tee /etc/apache2/conf-available/fqdn.conf
RUN ln -s /etc/apache2/conf-available/fqdn.conf /etc/apache2/conf-enabled/fqdn.conf
RUN ln -s /etc/apache2/sites-available/nagios.conf /etc/apache2/sites-enabled/


### Configuracion
### Usuario nagiosadmin pass 1234
COPY ./default-config/default_confg.tar.gz /tmp/default_confg.tar.gz
RUN tar zxvf /tmp/default_confg.tar.gz
RUN rm -rf /usr/local/nagios/etc
RUN mv /tmp/etc /usr/local/nagios

#### Optionals Modules
RUN apt-get update -y --fix-missing
RUN apt-get install -y libb-utils-perl libstring-random-perl python  libio-socket-ssl-perl libxml-simple-perl
RUN apt-get install -y snmp python-axolotl python-dateutil python-setuptools
RUN apt-get install -y python-dev libffi-dev libssl-dev libmonitoring-plugin-perl
RUN easy_install pip
RUN pip install python-axolotl
RUN pip install twx.botapi
RUN pip install urllib3
RUN pip install pyopenssl
RUN apt-get install -y make libperl-dev libparams-validate-perl libmath-calc-units-perl libclass-accessor-perl libconfig-tiny-perl git
WORKDIR /tmp
RUN git clone https://github.com/nagios-plugins/nagios-plugin-perl.git
WORKDIR /tmp/nagios-plugin-perl
RUN perl Makefile.PL
RUN make
RUN make test
RUN make install


### Personalizacion
RUN echo "alias l='ls -la'" >> /root/.bashrc
RUN echo "export TERM=xterm" >> /root/.bashrc
RUN wget https://www.alferez.es/nagios_logos/dockerbyalferez.png -O /usr/local/nagios/share/images/dockerbyalferez.png
RUN wget https://www.alferez.es/nagios_logos/sblogo.png -O /usr/local/nagios/share/images/sblogo.png
RUN wget https://www.alferez.es/nagios_logos/logofullsize.png -O /usr/local/nagios/share/images/logofullsize.png
RUN wget https://www.alferez.es/nagios_logos/corelogo.gif -O /usr/local/nagios/share/images/corelogo.gif
RUN sed -i '/<div class="logos">/a\                <a href="https:\/\/www.alferez.es\/" target="_blank"><img src="images\/dockerbyalferez.png" width="110" height="50" border="1" alt="Alferez.es" \/><\/a>' /usr/local/nagios/share/main.php
RUN sed -i 's/sblogo.png" height="39"/sblogo.png" height="52"/g' /usr/local/nagios/share/side.php


### Fix Mail Sender
RUN apt-get remove --purge -y exim4*
RUN apt-get install -y --fix-missing postfix
RUN apt-get install -y --fix-missing mailutils
RUN postconf -e mynetworks="0.0.0.0/0"
ENV ROOT_EMAIL=nagios@nagiossystem.com
ENV MAILNAME=nagios.nagiossystem.com
RUN postconf -e myhostname=$MAILNAME
RUN echo $MAILNAME > /etc/mailname
RUN echo root: $ROOT_EMAIL >> /etc/aliases
RUN /usr/bin/newaliases


### Limpiamos
RUN apt-get autoremove -y
RUN apt-get clean
RUN rm -rf /tmp/* /var/tmp/*
RUN rm -rf /var/lib/apt/lists/*

### Add Entrypoing
COPY ./assets/start.sh /start.sh
RUN chmod +x /start.sh

WORKDIR /root

ENTRYPOINT "/start.sh"
