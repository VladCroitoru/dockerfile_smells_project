FROM centos:centos7
MAINTAINER Viacheslav Pryimak <vpryimak@intropro.com>


################## BEGIN INSTALLATION ######################
RUN yum -y update && yum clean all && \
    yum -y install epel-release && yum -y update && \
    yum -y install sudo mc net-tools supervisor openssh-server openssh-clients mariadb \
    bind-utils bzip2 curl e2fsprogs expect bind-utils bzip2 curl git gitflow krb5-libs krb5-workstation libselinux-python \
    libstdc++ lsof net-tools nmap ntp openldap-clients psmisc python-pip python-setuptools sysstat tmux tar unzip vim-common vim wget && \
    yum clean all && \
    groupadd -r dap &&  useradd -c "dap" -d /opt/dap -g dap -s /bin/bash dap && ssh-keygen -A
##################### INSTALLATION END #####################

ADD ./sudo.dap /etc/sudoers.d/dap
ADD ./supervisord.conf /etc/supervisord.conf
ADD ./start.sh /start.sh
ADD ./data/scripts /opt/dap/scripts
RUN chmod +x /start.sh
RUN sed -i '/pam_loginuid\.so/s/required/optional/' /etc/pam.d/sshd
RUN chmod 755 /opt/dap && cd /opt/dap && ln -s install/apache-tomcat-8.0.20 tomcat && ln -s install/flyway-3.1 flyway && mkdir dap-log repository  && touch dap-log/dap.log && chown -R dap:dap /opt/dap

EXPOSE 22

ENTRYPOINT ["/start.sh"]