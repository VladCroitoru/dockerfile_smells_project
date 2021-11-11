FROM centos:centos7
MAINTAINER dayreiner

ENV HOME=/root \
    MARIADB_MAJOR=10.1 \
    AUTHORIZED_KEYS=**None**

# MariaDB Repo
COPY config/MariaDB.repo /etc/yum.repos.d/MariaDB.repo

# Install required packages and MariaDB Vendor Repo
RUN yum -y update && yum clean all && \
    yum -y install openssh-server epel-release && \
    yum clean all && \
    yum -y install pwgen python-setuptools && \
    yum -y install MariaDB-server MariaDB-client && yum clean all

# Add scripts as a directory vs individual adds for optimization
ADD scripts/ /
# supervisord config
COPY config/supervisord.conf /etc/supervisord.conf

# Setup SSH, supervisord and SQL setup
RUN echo "Setting up sshd..." && \
    rm -f /etc/ssh/ssh_host_ecdsa_key /etc/ssh/ssh_host_rsa_key && \
    ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_ecdsa_key && \
    ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key && \
    sed -i "s/#UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && \
    echo "Seting up supervisord..." && \
    chmod 666 /etc/supervisord.conf && \
    easy_install supervisor && \
    echo "Setting up MariDB database initialization scripts..." && \
    mkdir /docker-entrypoint-initdb.d && \
    chmod +x /*.sh && \
    /ssh-setup.sh

# MariaDB Config and DB Setup Scripts
COPY config/server.cnf /etc/my.cnf.d/server.cnf

# MariaDB volume and go
VOLUME /var/lib/mysql
EXPOSE 3306 22
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["mysqld"]
