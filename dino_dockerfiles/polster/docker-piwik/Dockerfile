FROM centos:centos7

MAINTAINER simon.dietschi@bluecare.ch

ENV PIWIK_VERSION 2.14.3

# install dependencies
RUN yum -y update && yum clean all \
  && yum -y install unzip php php-pdo php-mysql php-pgsql php-bcmath php-gd php-mbstring php-xml httpd-tools httpd \
  && yum clean all

# download and deploy piwik
RUN cd /opt/ \
  && curl -o piwik.zip -fSL http://builds.piwik.org/piwik-$PIWIK_VERSION.zip \
  && unzip piwik.zip -d /var/www/html/ \
  && rm piwik.zip*

# Adjust file system privileges
RUN chown -R apache:apache /var/www \
  && chmod -R 755 /var/www/html/piwik/tmp \
  && chmod -R 755 /var/www/html/piwik/config

# Adjust file system if SELinux is enabled
# RUN chcon -R -t httpd_sys_rw_content_t /var/www/html/piwik/tmp \
#   && chcon -R -t httpd_sys_rw_content_t /var/www/html/piwik/config

# http port
EXPOSE 80

ADD run-httpd.sh /run-httpd.sh
RUN chmod -v +x /run-httpd.sh

CMD ["/run-httpd.sh"]
