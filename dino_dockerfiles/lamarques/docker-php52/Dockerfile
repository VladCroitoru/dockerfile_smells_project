FROM centos:5
LABEL maintainer=" Rogerio Lamarques <rogerio.lamarques@gmail.com>"

COPY assets/init.sh /init.sh
COPY assets/utterramblings.repo /etc/yum.repos.d/utterramblings.repo
COPY assets/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo
COPY assets/CentOS-Debuginfo.repo /etc/yum.repos.d/CentOS-Debuginfo.repo
COPY assets/CentOS-fasttrack.repo /etc/yum.repos.d/CentOS-fasttrack.repo
COPY assets/CentOS-Media.repo /etc/yum.repos.d/CentOS-Media.repo
COPY assets/CentOS-Sources.repo /etc/yum.repos.d/CentOS-Sources.repo
COPY assets/CentOS-Vault.repo /etc/yum.repos.d/CentOS-Vault.repo
COPY assets/libselinux.repo /etc/yum.repos.d/libselinux.repo

RUN rpm --import http://vault.centos.org/RPM-GPG-KEY-CentOS-5
RUN yum clean all 
RUN yes | yum update -y
RUN yum install -y epel-release
RUN yes | yum upgrade
RUN yum install -y yum-utils
RUN yum install -y httpd vixie-cron syslog \
	php php-apc php-cli php-common php-gd php-mbstring php-mcrypt \
	php-mysql php-odbc php-pdo php-pear php-pear-DB php-soap php-xml php-xmlrpc php-imap \
	php-pdo 
RUN yum install -y php-pgsql
RUN yum install -y php-pdo_pgsql-5.2.17

RUN mkdir /etc/httpd/vhost.d && \
	echo "Include vhost.d/*.conf" >> /etc/httpd/conf/httpd.conf && \
	chmod +x /init.sh

EXPOSE 80 443

ENTRYPOINT ["/usr/sbin/httpd", "start"]