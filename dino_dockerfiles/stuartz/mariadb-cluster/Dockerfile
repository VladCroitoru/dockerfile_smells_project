FROM debian:jessie

MAINTAINER "Stuart Zurcher" <https://github.com/stuartz-VernonCo>
# using combination of code from official maraidb docker-library


# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added

# install "pwgen" for randomizing passwords
# add repository pinning to make sure dependencies from this MariaDB repo are preferred over Debian dependencies
# libmariadbclient18 : Depends: libmysqlclient18 (= 5.5.42+maria-1~wheezy) but 5.5.43-0+deb7u1 is to be installed

# the "/var/lib/mysql" stuff here is because the mysql-server postinst doesn't have an explicit way to disable the mysql_install_db codepath besides having a database already "configured" (ie, stuff in /var/lib/mysql/mysql)
# also, we set debconf keys to make APT a little quieter

# comment out a few problematic configuration values
# don't reverse lookup hostnames, they are usually another container

ENV MARIADB_MAJOR 10.1
ENV MARIADB_REPO mariadb-10.1.22
ENV MARIADB_PACKAGE 10.1.22+maria-1~jessie

RUN groupadd -r mysql && useradd -r -g mysql mysql \
    && apt-get update && apt-get upgrade -y \
    && apt-get install -y software-properties-common wget \
    && apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xcbcb082a1bb943db \
    && add-apt-repository "deb [arch=amd64,i386] http://mirror.nodesdirect.com/mariadb/$MARIADB_REPO/repo/debian/ jessie main" \
	&& { \
		echo 'Package: *'; \
		echo 'Pin: release o=MariaDB'; \
		echo 'Pin-Priority: 999'; \
	} > /etc/apt/preferences.d/mariadb \
	&&{ \
		echo mariadb-server-$MARIADB_MAJOR mysql-server/root_password password 'unused'; \
		echo mariadb-server-$MARIADB_MAJOR mysql-server/root_password_again password 'unused'; \
	} | debconf-set-selections \
  && wget https://repo.percona.com/apt/percona-release_0.1-4.$(lsb_release -sc)_all.deb \
	&& dpkg -i percona-release_0.1-4.jessie_all.deb \
	&& apt-get update \
	&& apt-get install -y pwgen wget ntp ntpdate\
		mariadb-server=$MARIADB_PACKAGE \
		openssl nano netcat-traditional socat pv locate \
        libpwquality-tools cracklib-runtime \
    	percona-xtrabackup-24 \
        sendmail sendmail-cf m4 \
	&& rm -rf /var/lib/apt/lists/* \
	&& rm -rf /var/lib/mysql

COPY my.cnf /etc/mysql/my.cnf
COPY galeranotify.py datadog.sh /etc/

COPY docker-entrypoint.sh /
# added chmod because of weird permission issue
RUN mkdir -p /docker-entrypoint-initdb.d \
    && chmod 550 /docker-entrypoint.sh \
    && service ntp start \
	&& ln -sf /usr/share/zoneinfo/America/Chicago /etc/localtime \
    && chown mysql:mysql /etc/galeranotify.py \
    && chmod 555 /etc/galeranotify.py
ENTRYPOINT ["/docker-entrypoint.sh"]
EXPOSE 3306 4444 4567 4567/udp 4568
