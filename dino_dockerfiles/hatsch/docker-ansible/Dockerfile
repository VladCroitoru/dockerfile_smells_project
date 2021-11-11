FROM ubuntu-upstart:14.04
MAINTAINER Stefan Hageneder <hatsch@gmail.com>

# Install Ansible and Git.
RUN apt-get update && \
  apt-get install --no-install-recommends -y software-properties-common && \
  apt-add-repository ppa:ansible/ansible && \
  apt-get update && \
  apt-get install -y ansible git && \
  echo '[local]\nlocalhost ansible_connection=local\n' > /etc/ansible/hosts && \
  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
