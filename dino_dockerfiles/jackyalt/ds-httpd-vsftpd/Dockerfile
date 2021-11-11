FROM centos:latest
MAINTAINER Jacky AT

# Install supervisor
RUN \
  yum update -y && \
  yum install -y epel-release && \
  yum install -y iproute python-setuptools hostname inotify-tools yum-utils which jq && \
  yum clean all && \
  
  easy_install supervisor

# Updating system and install some basic web-related tools
RUN \
yum update -y && \
yum install -y wget patch tar bzip2 unzip MariaDB-client

# Install apache server
RUN yum update -y
RUN yum install -y httpd
EXPOSE 80

# Install ftp server
RUN yum -y update && yum clean all
RUN yum -y install vsftpd 
EXPOSE 20 21

# Clean YUM caches to minimize Docker image size
RUN \
yum clean all && rm -rf /tmp/yum*

# Assign environment variables to create user and password (supervisor)
ENV USER=jacky
ENV PASSWORD=iaw

# Add index.html 
ADD html/* /var/www/html/

# Add vsftpd.conf and directory of anonymous users
ADD vsftpd.conf /etc/vsftpd/
RUN mkdir -p /var/lftp/pub
RUN chmod -R 777 /var/lftp/pub

# Add vsftpd.service file
ADD /container-files/vsftpd.service /usr/lib/systemd/system/

# Add supervisord conf, bootstrap.sh
ADD container-files /

# Execute the sed command to assign the values of the environment variable by default or some specific ones by the user in the file /etc/supervisord.conf and /config/init/supervisor_setcre.sh
RUN \
sed -ri "s/jacky/${USER}/g" /etc/supervisord.conf && \
sed -ri "s/iaw/${PASSWORD}/g" /etc/supervisord.conf && \
sed -ri "s/jacky/${USER}/g" /config/init/supervisor_setcre.sh && \
sed -ri "s/iaw/${PASSWORD}/g" /config/init/supervisor_setcre.sh

# Expose supervisor port
EXPOSE 9001
# To execute the script
ENTRYPOINT ["/config/bootstrap.sh"]



