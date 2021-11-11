FROM centos:6
MAINTAINER Juan Enciso <juan.enciso@gmail.com>
# install repo
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
RUN rpm -Uvh http://repo.webtatic.com/yum/el6/latest.rpm
# install httpd
RUN yum -y install httpd sed php56w php56w-mysql php56w-mcrypt php56w-pdo php56w-odbc php56w-mbstring php56w-pear php56w-devel php56w-dom php56w-intl php56w-mssql php56w-xml php56w-mcrypt php56w-pear php56w-soap && yum clean all && rm -rf /var/cache/yum

RUN service httpd start

ENV LOG_STDOUT **Boolean**
ENV LOG_STDERR **Boolean**
ENV LOG_LEVEL warn
ENV ALLOW_OVERRIDE All
ENV DATE_TIMEZONE UTC

COPY index.php /var/www/html/
COPY run-lap.sh /usr/sbin/
RUN chmod +x /usr/sbin/run-lap.sh
RUN chown -R apache:apache /var/www/html

VOLUME /var/www/html
VOLUME /var/log/httpd

EXPOSE 80

CMD ["/usr/sbin/run-lap.sh"]
