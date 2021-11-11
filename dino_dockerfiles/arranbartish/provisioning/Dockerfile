FROM ubuntu:16.04

MAINTAINER Arran Bartish <arranbartish@hotmail.com>

ENV HOSTS_LOCATION /ansible/files/hosts
ENV PLAYBOOK_LOCATION /ansible/files/

ADD ./files /ansible/files

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    apt-add-repository ppa:ansible/ansible && \
    apt-get update && \
    apt-get install -y ssh ansible && \
    mkdir -p /ansible/files && \
    adduser --disabled-password --gecos "ansible" --home /ansible --no-create-home ansible && \
    chown -R ansible:ansible /ansible && \
    ln -s /ansible/.ssh /ssh

WORKDIR /ansible

USER ansible

ENTRYPOINT ["/ansible/files/docker-entrypoint.sh"]
CMD ["tail", "-f", "/dev/null"]