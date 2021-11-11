FROM colinsung/c7-systemd

RUN yum -y update
RUN yum -y groupinstall core
# Workarround for cap_set_file(mtr) - error
RUN yum -y groupinstall base ; exit 0
RUN yum -y install epel-release
RUN yum -y install automake gcc gcc-c++ ncurses-devel openssl-devel libxml2-devel unixODBC-devel \
  libcurl-devel libogg-devel libvorbis-devel speex-devel spandsp-devel freetds-devel net-snmp-devel \
  iksemel-devel corosynclib-devel newt-devel popt-devel libtool-ltdl-devel lua-devel sqlite-devel \
  radiusclient-ng-devel portaudio-devel neon-devel libical-devel openldap-devel gmime-devel mysql-devel \
  bluez-libs-devel jack-audio-connection-kit-devel gsm-devel libedit-devel libuuid-devel jansson-devel \
  libsrtp-devel git subversion libxslt-devel kernel-devel audiofile-devel gtk2-devel libtiff-devel \
  libtermcap-devel ilbc-devel bison \
  tftp-server sox tzdata mysql-connector-odbc mariadb mariadb-server fail2ban jwhois
# Workarround for cap_set_file(httpd) - error
RUN yum -y install httpd php php-mysql php-process php-pear php-mbstring php-xml php-gd ; exit 0
RUN pear install Console_getopt
RUN sed -i 's/\(^SELINUX=\).*/\SELINUX=disabled/' /etc/selinux/config
# install asterisk
RUN adduser asterisk -s /sbin/nologin -c "Asterisk User"
RUN yum-config-manager --add-repo http://yum.freepbxdistro.org/pbx/10.13.66/x86_64/
RUN yum --nogpgcheck -y install asterisk13 asterisk13-configs
# for asterisk testsuite
RUN yum -y install PyYAML python-twisted-core python-setuptools
