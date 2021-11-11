FROM ubuntu:14.04
MAINTAINER Arnaud Blancher
RUN apt-get update -q \
 # ansible 2.1.1.0
 && apt-get install -y python-jinja2-doc  sshpass  libyaml-0-2 python-crypto python-ecdsa python-httplib2 python-paramiko python-selinux python-yaml python-pip python-apt \
 && pip install ansible==2.1.1.0 docker-py==1.9.0 \
 && pip install ansible-lint \
 # docker
 &&  apt-get install -y apt-transport-https ca-certificates \
 &&  apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D \
 &&  echo 'deb https://apt.dockerproject.org/repo ubuntu-trusty main' > /etc/apt/sources.list.d/docker.list \
 &&  apt-get update -q \
 &&  apt-get purge - lxc-docker \
 # locales
 && locale-gen fr_FR.UTF-8 && locale-gen en_US.UTF-8 \
 && update-locale && dpkg-reconfigure locales \
 # &&  apt-get install -y apparmor docker-engine
 # tester la docker-engine=1.12.3-0~trusty
 &&  apt-get install -y apparmor docker-engine=1.11.2-0~trusty

CMD ["/bin/bash"]
