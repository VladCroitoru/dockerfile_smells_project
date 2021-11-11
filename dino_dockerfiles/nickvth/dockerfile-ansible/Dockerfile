# Get latest centos7.x image from official centos docker repo.
FROM centos:centos7

# Set Maintainer of this Dockerfile.
MAINTAINER nickvth

# Update os to the latest version.
RUN yum -y update

# Install needed packages.
RUN yum -y install epel-release 
RUN yum -y install ansible openssh openssh-clients sshpass; yum clean all
RUN mkdir /root/.ssh && chown 640 /root/.ssh
ADD ansible.cfg /etc/ansible/ansible.cfg
ADD ssh-agent.sh /ssh-agent.sh
RUN chmod +x /ssh-agent.sh
WORKDIR /mnt
CMD ["/usr/bin/ansible --version"]
