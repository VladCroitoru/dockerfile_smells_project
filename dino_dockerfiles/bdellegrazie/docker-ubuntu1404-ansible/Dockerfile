FROM ubuntu:14.04
MAINTAINER "Brett Delle Grazie" <brett.dellegrazie@gmail.com>
ENV container=docker DEBIAN_FRONTEND=noninteractive DEBIAN_PRIORITY=critical LANG=C.UTF-8

# Limit auto-installed dependencies
RUN echo 'APT::Install-Recommends "0";\nAPT::Get::Assume-Yes "true";\nAPT::Get::force-yes "true";\nAPT::Install-Suggests "0";\n' > /etc/apt/apt.conf.d/01buildconfig

RUN apt-get -y -qq update &&\
 apt-get -y -qq install apt-utils software-properties-common &&\
 apt-get -y -qq clean &&\
 rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Ansible and other requirements.
RUN add-apt-repository -y ppa:ansible/ansible &&\
 apt-get -y -qq update &&\
 apt-get -y -qq install sudo curl net-tools ansible &&\
 apt-get -y -qq clean &&\
 rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN sed -i -e 's/^\(Defaults\s*requiretty\)/#--- \1/' /etc/sudoers

# Install Ansible inventory file.
RUN echo '[local]\nlocalhost ansible_connection=local' > /etc/ansible/hosts

# put initctl back
RUN rm -f /sbin/initctl && dpkg-divert --local --rename --remove /sbin/initctl

VOLUME ["/sys/fs/cgroup"]
CMD ["/sbin/init"]
