FROM ubuntu:12.04
MAINTAINER "Brett Delle Grazie" <brett.dellegrazie@gmail.com>
ENV container=docker DEBIAN_FRONTEND=noninteractive DEBIAN_PRIORITY=critical LANG=C.UTF-8

# Install dependencies.
RUN apt-get -y -qq update &&\
 apt-get -y -qq install apt-utils software-properties-common python-software-properties &&\
 rm -Rf /usr/share/doc &&\
 rm -Rf /usr/share/man &&\
 apt-get -y -qq clean &&\
 rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Ansible and other requirements.
RUN add-apt-repository -y ppa:ansible/ansible &&\
 apt-get -y -qq update &&\
 apt-get -y -qq install sudo net-tools curl ansible &&\
 rm -Rf /usr/share/doc &&\
 rm -Rf /usr/share/man &&\
 apt-get -y -qq clean &&\
 rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Ansible inventory file
RUN echo "[local]\nlocalhost ansible_connection=local" > /etc/ansible/hosts

# put initctl back
RUN rm -f /sbin/initctl && dpkg-divert --local --rename --remove /sbin/initctl
