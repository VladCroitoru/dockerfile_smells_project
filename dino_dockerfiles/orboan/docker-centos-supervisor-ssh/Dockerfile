FROM centos:7.3.1611
MAINTAINER Oriol Boix Anfosso dev@orboan.com

# - Install basic packages (e.g. python-setuptools is required to have python's easy_install)
# - Install yum-utils so we have yum-config-manager tool available
# - Install inotify, needed to automate daemon restarts after config file changes
# - Install jq, small library for handling JSON files/api from CLI
# - Install supervisord (via python's easy_install - as it has the newest 3.x version)
RUN \
  yum update -y && \
  yum install -y epel-release && \
  yum install -y iproute python-setuptools hostname inotify-tools yum-utils which jq && \
  yum clean all && \

  easy_install supervisor

# - Updating system
# - Install some basic web-related tools...
RUN \ 
yum update -y && \ 
yum install -y wget patch tar bzip2 unzip openssh-clients MariaDB-client

# - Install OpenSSH server
RUN \
  yum install -y openssh-server pwgen sudo vim mc links

# - Generate keys for ssh. 
# (This is usually done by systemd when sshd service is started)
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N '' \
&& ssh-keygen -t dsa  -f /etc/ssh/ssh_host_dsa_key -N '' \
&& ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -N '' \
&& chmod 600 /etc/ssh/*

# - Configure SSH daemon...
RUN \
  sed -i -r 's/.?UseDNS\syes/UseDNS no/' /etc/ssh/sshd_config && \
  sed -i -r 's/.?PasswordAuthentication.+/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
  sed -i -r 's/.?ChallengeResponseAuthentication.+/ChallengeResponseAuthentication no/' /etc/ssh/sshd_config && \
  sed -i -r 's/.?PermitRootLogin.+/PermitRootLogin no/' /etc/ssh/sshd_config

# - Adding keyfiles configuration
RUN \
  sed -ri 's/^HostKey\ \/etc\/ssh\/ssh_host_ed25519_key/#HostKey\ \/etc\/ssh\/ssh_host_ed25519_key/g' /etc/ssh/sshd_config && \
  sed -ri 's/^#HostKey\ \/etc\/ssh\/ssh_host_dsa_key/HostKey\ \/etc\/ssh\/ssh_host_dsa_key/g' /etc/ssh/sshd_config && \
  sed -ri 's/^#HostKey\ \/etc\/ssh\/ssh_host_rsa_key/HostKey\ \/etc\/ssh\/ssh_host_rsa_key/g' /etc/ssh/sshd_config && \
  sed -ri 's/^#HostKey\ \/etc\/ssh\/ssh_host_ecdsa_key/HostKey\ \/etc\/ssh\/ssh_host_ecdsa_key/g' /etc/ssh/sshd_config && \
  sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

# Disable SSH strict host key checking: needed to access git via SSH in non-interactive mode
RUN \
  echo -e "StrictHostKeyChecking no" >> /etc/ssh/ssh_config

# - Remove 'Defaults secure_path' from /etc/sudoers which overrides path when using 'sudo' command
RUN \
  sed -i '/secure_path/d' /etc/sudoers

# - Remove warning about missing locale while logging in via ssh
RUN \
  echo > /etc/sysconfig/i18n

# - Colorize ls
RUN echo 'alias ls="ls --color"' >> ~/.bashrc \
&& echo 'alias ll="ls -lh"' >> ~/.bashrc \
&& echo 'alias la="ls -lha"' >> ~/.bashrc

# - Clean YUM caches to minimise Docker image size...
RUN \
  yum clean all && rm -rf /tmp/yum*

ENV USER=www
ENV PASSWORD=iaw

# - Add supervisord conf, bootstrap.sh files
ADD container-files /

RUN \
   sed -ri "s/www/${USER}/g" /etc/supervisord.conf && \
   sed -ri "s/iaw/${PASSWORD}/g" /etc/supervisord.conf

VOLUME ["/data"]

EXPOSE 22 9001

ENTRYPOINT ["/config/bootstrap.sh"]
