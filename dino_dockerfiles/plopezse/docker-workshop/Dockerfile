# Set the base image to Fedora
FROM docker.io/centos

# File Author / Maintainer
MAINTAINER "Pedro Lopez" "plopezse@redhat.com"

RUN yum install -y --setopt=tsflags=nodocs httpd && yum clean all

EXPOSE 80
VOLUME /var/www/html

CMD ["/usr/sbin/apachectl" "-D" "FOREGROUND"]
