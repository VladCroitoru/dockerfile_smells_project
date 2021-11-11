FROM alpine as ioncube_loader
RUN apk add git \
	&& git -c http.sslVerify=false clone https://git.dev.glo.gb/cloudhostingpublic/ioncube_loader \
	&& tar zxf ioncube_loader/ioncube_loaders_lin_x86-64.tar.gz

FROM 1and1internet/ubuntu-16:latest
MAINTAINER brian.wilkinson@1and1.co.uk
ARG DEBIAN_FRONTEND=noninteractive
COPY files /

# Mongodb client + tools
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \
            --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5 && \
    apt-get update && \
    apt-get install -y mongodb-org-shell mongodb-org-tools && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
    apt-get update && \
    apt-get install -y postgresql-client-10 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY --from=ioncube_loader /ioncube/ioncube_loader_lin_7.2.so /usr/lib/php/20170718/

RUN \
  apt-get update && \
  apt-get install -y python-software-properties software-properties-common && \
  LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php && \
  apt-get update && \
  apt-get install -y \
    libapache2-mod-php7.0 mysql-client libmysqlclient-dev perl ruby ruby-dev rake zlib1g-dev sqlite sqlite3 \
    git vim traceroute telnet nano dnsutils curl wget iputils-ping openssh-client openssh-sftp-server \
    virtualenv python3-venv python3-virtualenv python3-all python3-setuptools python3-pip python-dev python3-dev python-pip \
    gnupg build-essential ruby2.3-dev libsqlite3-dev redis-tools && \
  apt-get install -y imagemagick graphicsmagick && \
  apt-get install -y php5.6-bcmath php5.6-bz2 php5.6-cli php5.6-common php5.6-curl php5.6-dba php5.6-gd php5.6-gmp php5.6-imap php5.6-intl php5.6-ldap php5.6-mbstring php5.6-mcrypt php5.6-mysql php5.6-odbc php5.6-pgsql php5.6-recode php5.6-snmp php5.6-soap php5.6-sqlite php5.6-tidy php5.6-xml php5.6-xmlrpc php5.6-xsl php5.6-zip && \
  apt-get install -y php7.0-bcmath php7.0-bz2 php7.0-cli php7.0-common php7.0-curl php7.0-dba php7.0-gd php7.0-gmp php7.0-imap php7.0-intl php7.0-ldap php7.0-mbstring php7.0-mcrypt php7.0-mysql php7.0-odbc php7.0-pgsql php7.0-recode php7.0-snmp php7.0-soap php7.0-sqlite php7.0-tidy php7.0-xml php7.0-xmlrpc php7.0-xsl php7.0-zip && \
  apt-get install -y php7.1-bcmath php7.1-bz2 php7.1-cli php7.1-common php7.1-curl php7.1-dba php7.1-gd php7.1-gmp php7.1-imap php7.1-intl php7.1-ldap php7.1-mbstring php7.1-mcrypt php7.1-mysql php7.1-odbc php7.1-pgsql php7.1-recode php7.1-snmp php7.1-soap php7.1-sqlite php7.1-tidy php7.1-xml php7.1-xmlrpc php7.1-xsl php7.1-zip && \
  apt-get install -y php7.2-bcmath php7.2-bz2 php7.2-cli php7.2-common php7.2-curl php7.2-dba php7.2-gd php7.2-gmp php7.2-imap php7.2-intl php7.2-ldap php7.2-mbstring php7.2-mysql php7.2-odbc php7.2-pgsql php7.2-recode php7.2-snmp php7.2-soap php7.2-sqlite php7.2-tidy php7.2-xml php7.2-xmlrpc php7.2-xsl php7.2-zip && \
  apt-get install -y php7.3-bcmath php7.3-bz2 php7.3-cli php7.3-common php7.3-curl php7.3-dba php7.3-gd php7.3-gmp php7.3-imap php7.3-intl php7.3-ldap php7.3-mbstring php7.3-mysql php7.3-odbc php7.3-pgsql php7.3-recode php7.3-snmp php7.3-soap php7.3-sqlite php7.3-tidy php7.3-xml php7.3-xmlrpc php7.3-xsl php7.3-zip && \
  apt-get install -y php-gnupg php-imagick php-mongodb php-streams php-fxsl && \
  apt-get install -y curl apt-transport-https ca-certificates lsb-release && \
  DISTRO=$(lsb_release -c -s) && \
  NODEREPO="node_6.x" && \
  curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && \
  echo "deb https://deb.nodesource.com/${NODEREPO} ${DISTRO} main" > /etc/apt/sources.list.d/nodesource.list && \
  echo "deb-src https://deb.nodesource.com/${NODEREPO} ${DISTRO} main" >> /etc/apt/sources.list.d/nodesource.list && \
  apt-get update -q && \
  apt-get install -y build-essential nodejs && \
  apt-get remove -y python-software-properties software-properties-common && \
  apt-get autoremove -y && apt-get autoclean -y && \
  chmod 0777 /var/www && \
  mkdir /tmp/composer/ && \
  cd /tmp/composer && \
  curl -sS https://getcomposer.org/installer | php && \
  mv composer.phar /usr/local/bin/composer && \
  rm -rf /tmp/composer && \
  rm -rf /var/lib/apt/lists/* && \
  chmod 0755 /usr/local/bin/composer && \
  chmod 0755 -R /hooks /init && \
  chmod 0777 /etc/passwd /etc/group && \
  mkdir --mode 0777 /usr/local/composer && \
  COMPOSER_HOME=/usr/local/composer /usr/local/bin/composer --no-ansi --no-interaction global require drush/drush:8.* && \
  COMPOSER_HOME=/usr/local/composer /usr/local/bin/composer --no-ansi --no-interaction global clearcache && \
  mv /usr/bin/cpan /usr/bin/cpan_disabled && \
  mv /usr/bin/cpan_override /usr/bin/cpan && \
  rm -f /etc/ssh/ssh_host_* && \
  chmod -R 0777 /etc/supervisor/conf.d

ENV COMPOSER_HOME=/var/www \
    HOME=/var/www

WORKDIR /var/www

# Install and configure the cron service
ENV EDITOR=/usr/bin/vim \
	CRON_LOG_FILE=/var/spool/cron/cron.log \
	CRON_LOCK_FILE=/var/spool/cron/cron.lock \
	CRON_ARGS=""
RUN \
  apt-get update && apt-get install -y -o Dpkg::Options::="--force-confold" logrotate man && \
  cd /src/cron-3.0pl1 && \
  make install && \
  mkdir -p /var/spool/cron/crontabs && \
  chmod -R 777 /var/spool/cron && \
  cp debian/crontab.main /etc/crontab && \
  cd - && \
  rm -rf /src && \
  find /etc/cron.* -type f | egrep -v 'logrotate|placeholder' | xargs -i rm -f {} && \
  chmod 666 /etc/logrotate.conf && \
  chmod -R 777 /var/lib/logrotate && \
  rm -rf /var/lib/apt/lists/*
