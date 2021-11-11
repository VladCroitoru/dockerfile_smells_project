FROM quay.io/ansible/awx-ee:0.5.0

USER root

# add Python dependencies and Ansible
# Galary dependencies
ADD requirements.yml /tmp/requirements.yml
ADD requirements.txt /tmp/requirements.txt
ADD snmp_facts.py.patch /tmp/snmp_facts.py.patch

# upgrade pip
RUN /usr/bin/python3 -m pip install --upgrade pip

# install Ansible Galaxy collections
RUN ansible-galaxy collection install -r /tmp/requirements.yml --collections-path /usr/share/ansible/collections

# install Python dependencies
RUN pip install -r /tmp/requirements.txt

# Apply snmp_facts pach
RUN dnf install -y patch
RUN patch /usr/share/ansible/collections/ansible_collections/community/general/plugins/modules/net_tools/snmp_facts.py /tmp/snmp_facts.py.patch
#RUN patch /usr/share/ansible/collections/ansible_collections/community/general/plugins/modules/snmp_facts.py /tmp/snmp_facts.py.patch

RUN dnf install -y expect

USER 1000
