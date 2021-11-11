FROM million12/nginx-php:latest
MAINTAINER jbrunicardi@gmail.com

RUN \
  yum update -y && \
  
  `# Install sendmail, memcached, (php-memcache already installed in base image)#` \
  yum install -y sendmail memcached \
  
  `# Temporary workaround: one dependant package fails to install when building image (and the yum error is: Error unpacking rpm package httpd-2.4.6-40.el7.centos.x86_64)...` \
  || true && \
  
  `# Clean YUM caches to minimise Docker image size... #` \
  yum clean all && rm -rf /tmp/yum*

ADD container-files /