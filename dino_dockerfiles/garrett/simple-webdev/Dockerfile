FROM centos:latest
MAINTAINER Garrett LeSage <garrett@lesage.us>

# Install required packages, including pdo for sqlite
RUN yum -y install httpd php php-pdo php-xml php-gd php-mbstring yum-security

# Install all security updates
RUN yum -y update --security

RUN echo 'LANG="en_US.UTF-8"' >/etc/default/locale

# Enable .htaccess everywhere, to make development easier
RUN sed 's/AllowOverride None/AllowOverride All/i' /etc/httpd/conf/httpd.conf > httpd.conf
RUN mv httpd.conf /etc/httpd/conf/httpd.conf

# Send port 80 (web) out to the real world
EXPOSE 80

# Run Apache
ENTRYPOINT ["/usr/sbin/httpd"]

# By default: don't detatch; make control-c work
CMD ["-DNO_DETACH"]
