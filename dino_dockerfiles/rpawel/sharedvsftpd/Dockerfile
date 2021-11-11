# runnable base
FROM ubuntu:trusty

# REPOS
RUN apt-get -y update && locale-gen en_GB.UTF-8
RUN echo "Europe/London" | tee /etc/timezone; dpkg-reconfigure --frontend noninteractive tzdata
RUN apt-get install -y -q software-properties-common

RUN add-apt-repository -y "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) multiverse"
RUN add-apt-repository -y "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc)-updates multiverse"

RUN apt-get -y update

# PACKAGES
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q vim nano curl git subversion wget unzip logrotate vsftpd libpam-pwdfile supervisor apache2-utils ftp

## CONFIG
# VsFTPd
ADD ./config/vsftpd.conf /etc/vsftpd.conf
ADD config/pam.d/vsftpd /etc/pam.d/vsftpd
ADD config/supervisord.conf /etc/supervisord.conf
RUN mkdir -p /var/run/vsftpd/empty && chown root:root /etc/vsftpd.conf

RUN sh -c "echo pasv_address=EXTERNAL.SERVER.IP.ADDRESS >> /etc/vsftpd.conf"
RUN sh -c "echo pasv_min_port=49210 >> /etc/vsftpd.conf"
RUN sh -c "echo pasv_max_port=49210 >> /etc/vsftpd.conf"

# Supervisord
RUN mkdir -p /var/log/supervisor; mkdir /etc/vsftpd; ln -s /var/www/config/passwd /etc/vsftpd/passwd; usermod -u 1000 ftp; usermod -g www-data ftp

EXPOSE 21 49210
## START
ADD config/run.sh /
RUN chmod +x /run.sh

ENTRYPOINT ["/run.sh"]
