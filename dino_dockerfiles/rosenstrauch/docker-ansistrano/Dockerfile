FROM phusion/baseimage

MAINTAINER Nil Portugués Calderó <contact@nilportugues.com>

CMD ["/sbin/my_init"]

RUN apt-get -y update
RUN apt-get -y install software-properties-common
RUN apt-add-repository -y ppa:ansible/ansible
RUN apt-get -y update
RUN apt-get -y install ansible openssh-client rsync
RUN ansible-galaxy install --force carlosbuenosvinos.ansistrano-deploy carlosbuenosvinos.ansistrano-rollback --roles-path=/usr/share/ansible/roles

## Ansistrano user
RUN adduser --disabled-password --gecos '' ansistrano
RUN adduser ansistrano sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

## Ansistrano folder
RUN mkdir -p /home/ansistrano/.ssh
RUN cd /home/ansistrano/.ssh/ && ssh-keygen -t rsa -b 4096 -C '' -f /home/ansistrano/.ssh/id_rsa
RUN chown ansistrano:ansistrano -Rf /home/ansistrano/
WORKDIR /home/ansistrano/

## Run as ansistrano inside the container by default
COPY start.sh /start.sh
ENTRYPOINT ["/start.sh"]

CMD [ "ansible" ]

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
