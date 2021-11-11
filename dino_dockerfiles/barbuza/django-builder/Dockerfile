FROM ubuntu:latest
MAINTAINER Victor Kotseruba <barbuzaster@gmail.com>
RUN locale-gen en_US en_US.UTF-8
RUN sed -i.bak 's/main$/main universe/' /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y --no-install-recommends python-software-properties
RUN add-apt-repository -y ppa:chris-lea/node.js
RUN apt-get update
RUN apt-get install -y --no-install-recommends curl wget git vim
RUN apt-get install -y --no-install-recommends supervisor openssh-server postgresql memcached nginx-light nodejs
RUN apt-get install -y --no-install-recommends python-pip python-virtualenv python-dev build-essential libjpeg-dev libpq-dev libmemcached-dev libncurses5-dev
RUN mkdir -p /var/run/sshd
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -s /bin/true /sbin/initctl
RUN pg_dropcluster 9.1 main
ADD postgres_init.sh /postgres_init.sh
ADD memcache_init.sh /memcache_init.sh
ADD nginx_init.sh /nginx_init.sh
RUN mkdir /root/.ssh
RUN chmod 700 /root/.ssh
ADD docker_rsa.pub /root/.ssh/authorized_keys
RUN chown root /root/.ssh/authorized_keys
RUN apt-get clean
RUN yes | ssh-keygen -q -t rsa -N "" -C docker -f /root/.ssh/id_rsa
EXPOSE 3000 3001 3002 22
CMD ["/usr/bin/supervisord"]
