# [START all]
# Create an enhanced and K8s-friendly Super NetOps container
FROM f5devcentral/f5-super-netops-container:base
RUN apk update && apk add ca-certificates && update-ca-certificates && apk add openssl
RUN apk add ansible
RUN apk add python
RUN pip install ansible
RUN pip install bigsuds
RUN pip install f5-sdk
RUN pip install netaddr

# create directories necessary for f5-ansible setup
RUN rm -rf /usr/share/ansible
RUN mkdir /usr/share/ansible
RUN mkdir ~/ansible
RUN mkdir ~/ansible/playbooks/
RUN mkdir ~/ansible/playbooks/files/
RUN cd ~/ansible/playbooks && wget https://raw.githubusercontent.com/mlowcher61/F5-Ansible/master/f5_ansible_setup.yml

# demonstrate that the above ran
RUN ls -lR /usr/share/ansible ~

# spin forever
CMD node
# [END all]
