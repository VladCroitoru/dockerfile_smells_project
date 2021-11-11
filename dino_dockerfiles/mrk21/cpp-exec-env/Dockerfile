FROM ubuntu:12.04
MAINTAINER Yuichi Murata <mrk21info+docker@gmail.com>

ADD ansible /var/lib/ansible
WORKDIR /var/lib/ansible
RUN ./install_ansible.sh
RUN ansible-playbook -vvvv -c local -i inventory.ini site.yml
