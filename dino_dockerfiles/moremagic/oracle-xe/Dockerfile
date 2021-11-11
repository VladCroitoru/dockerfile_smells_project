FROM centos:centos7
MAINTAINER moremagic <itoumagic@gmail.com>

RUN yum -y update
RUN yum upgrade -y ca-certificates

# Add Oracle requirements
RUN yum install -y libaio bc flex net-tools redhat-lsb openssh-server
#RUN mkdir -p /var/lock/subsys

# Install Oracle XE
# - Check RPM SHA1
# - Work around the Swap memory limitation
# - Work around the sysctl limitation of Docker
ADD oracle-xe-11.2.0-1.0.x86_64.rpm.* /tmp/
RUN cat /tmp/oracle-xe-11.2.0-1.0.x86_64.rpm.x* > /tmp/oracle-xe-11.2.0-1.0.x86_64.rpm \ 
    && sha1sum /tmp/oracle-xe-11.2.0-1.0.x86_64.rpm | grep -q "49e850d18d33d25b9146daa5e8050c71c30390b7" \
    && mv /usr/bin/free /usr/bin/free.bak \
    && printf "#!/bin/sh\necho Swap - - 2048" > /usr/bin/free \
    && chmod +x /usr/bin/free \
    && mv /sbin/sysctl /sbin/sysctl.bak \
    && printf "#!/bin/sh" > /sbin/sysctl \
    && chmod +x /sbin/sysctl \
    && rpm --install /tmp/oracle-xe-11.2.0-1.0.x86_64.rpm \
    && rm /tmp/oracle-xe-11.2.0-1.0.x86_64.rpm* \
    && rm /usr/bin/bc \
    && rm /usr/bin/free \
    && mv /usr/bin/free.bak /usr/bin/free \
    && rm /sbin/sysctl \
    && mv /sbin/sysctl.bak /sbin/sysctl

# Configure Oracle
RUN printf "\
ORACLE_HTTP_PORT=8080 \n\
ORACLE_LISTENER_PORT=1521 \n\
ORACLE_PASSWORD=oracle \n\
ORACLE_CONFIRM_PASSWORD=oracle \n\
ORACLE_DBENABLE=y \n\
" > /tmp/response \
    && sed -i -e 's/^\(memory_target=.*\)/#\1/' /u01/app/oracle/product/11.2.0/xe/config/scripts/initXETemp.ora \
    && sed -i -e 's/^\(memory_target=.*\)/#\1/' /u01/app/oracle/product/11.2.0/xe/config/scripts/init.ora \
    && /etc/init.d/oracle-xe configure responseFile=/tmp/response \
    && rm /tmp/response

# Configure OpenSSH & set a password for oracle user.
# You can change this password with:
# docker exec -ti oracle_app passwd oracle
RUN ssh-keygen -h -t rsa -f /etc/ssh/ssh_host_rsa_key \
    && ssh-keygen -h -t dsa -f /etc/ssh/ssh_host_dsa_key \
    && echo "root" | passwd --stdin root \
    && echo "oracle" | passwd --stdin oracle \
    && printf '\
export ORACLE_HOME=/u01/app/oracle/product/11.2.0/xe \n\
export PATH=$ORACLE_HOME/bin:$PATH \n\
export ORACLE_SID=XE \n\
' >> /etc/bash.bashrc

EXPOSE 22 1521 8080

CMD sed -i -E "s/HOST = [^)]+/HOST = $HOSTNAME/g" /u01/app/oracle/product/11.2.0/xe/network/admin/listener.ora; \
    /etc/init.d/oracle-xe start; \
    /usr/sbin/sshd -D
