FROM fedora

RUN \
  dnf \
    --assumeyes \
    install ansible tar openssh-clients &&\
  dnf clean all;

RUN \
  mkdir -p /usr/share/ansible/openshift-ansible/ &&\
  curl --location --silent https://github.com/openshift/openshift-ansible/archive/master.tar.gz | tar xzf - --strip-components 1 -C /usr/share/ansible/openshift-ansible/

ENV ANSIBLE_CONFIG="/usr/share/ansible/openshift-ansible/ansible.cfg"

ENTRYPOINT ["/usr/bin/bash"]
