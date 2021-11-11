FROM orboan/docker-centos-supervisor-ssh
MAINTAINER Oriol Boix Anfosso <dev@orboan.com>

RUN yum update -y && \
  yum install -y openssl shellinabox

# - Clean YUM caches to minimise Docker image size...
RUN \
  yum clean all && rm -rf /tmp/yum*

# This is the host port to map to the shellinabox exposed port (4200)
# You can override this default value with the -e option in 'docker run'
# Please choose the value for this env variable acordingly to the 
# mapped port with the option -p in 'docker run'
ENV SHELLINABOX_PORT=9100

ENV USER=www
ENV PASSWORD=iaw

ADD container-files /

EXPOSE 4200
