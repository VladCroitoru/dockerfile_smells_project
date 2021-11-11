FROM ubuntu:14.04
MAINTAINER Maestrano <it@maestrano.com>

# Install Ansible
RUN apt-get -y update &&  \
    apt-get -y upgrade &&  \
    apt-get -q -y --no-install-recommends install unattended-upgrades git \
              python-yaml python-jinja2 python-httplib2 python-keyczar \
              python-paramiko python-setuptools python-pkg-resources python-pip &&  \
    mkdir -p /etc/ansible/ &&  \
    pip install ansible==1.9.6

# Add ansible configuration
ADD ansible /etc/ansible
WORKDIR /etc/ansible

# Run Ansible
RUN ansible-playbook -vvv -i hosts site.yml &&  \
    apt-get clean purge -y python2.6 python2.6-minimal &&  \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Expose port 22 and 80
EXPOSE 22 80

# Configuration scripts
ADD /scripts/ /root/

# Startup script to run mysql and apache
ADD /scripts/init.sh /root/init.sh
RUN chmod 755 /root/init.sh

# Map mutable volumes
VOLUME ["/etc/ansible"]

ENTRYPOINT ["/root/init.sh"]
CMD ["/root/init.sh"]
