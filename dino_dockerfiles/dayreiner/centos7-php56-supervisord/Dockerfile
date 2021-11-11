# K2 Generic Apache + PHP 5.6 + SSH Docker Base Image with github prep for code pulls to httpd docroot
# Uses supervisord to run sshd in addition to apache for convenience in development environments
#
FROM centos:latest
MAINTAINER dayreiner

ENV AUTHORIZED_KEYS **None**

# Update and install latest packages and prerequisites
RUN yum -y update && yum clean all && \
    yum -y install openssh-server epel-release git && \
    yum -y install https://mirror.webtatic.com/yum/el7/webtatic-release.rpm && yum clean all && \
    yum -y install pwgen httpd python-setuptools && \
    yum -y install composer php56w php56w-cli php56w-common php56w-opcache php56w-mysql php56w-mbstring && \
    yum clean all

# Setup Scripts
ADD scripts/ /

# Setup php.ini, supervisord conf and ssh key for git
COPY config/php.ini /etc/php.ini
COPY config/supervisord.conf /etc/supervisord.conf

# Setup SSH and SSHD
RUN rm -f /etc/ssh/ssh_host_ecdsa_key /etc/ssh/ssh_host_rsa_key && \
    ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_ecdsa_key && \
    ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key && \
    sed -i "s/#UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && \
    echo "Installing supervisord..." && \
    chmod 666 /etc/supervisord.conf && \
    easy_install supervisor && \
    echo "Setting up SSH for GitHub Checkouts..." && \
    mkdir -p /root/.ssh && chmod 700 /root/.ssh && \
    touch /root/.ssh/known_hosts && \
    ssh-keyscan -H github.com >> /root/.ssh/known_hosts && \
    chmod 600 /root/.ssh/known_hosts && \
    chmod +x /*.sh

RUN /ssh-setup.sh

EXPOSE 22 80
CMD ["/usr/bin/supervisord"]
