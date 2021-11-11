FROM ubuntu:xenial
MAINTAINER wale soyionka <wsoyinka@gmail.com>

ENV TERM=xterm-256color

RUN sed -i "s/http:\/\/archive./http:\/\/ca.archive./g" /etc/apt/sources.list

#Install Ansible

RUN 	apt-get update -qy && \
	apt-get install -qy software-properties-common && \
	apt-add-repository -y ppa:ansible/ansible && \
	apt-get update -qy && \
	apt-get install -qy ansible


COPY ansible /ansible

# volume for ansible playbooks

VOLUME /ansible
WORKDIR /ansible


#Entrypoint 

ENTRYPOINT ["ansible-playbook"]
CMD ["site.yml"]


