FROM ansible/centos7-ansible

# This playbook will install iRODS icommands from remote RPM
COPY install.yml /install.yml
COPY roles /roles
RUN ansible-playbook /install.yml -c local

USER iuser
WORKDIR /home/iuser

