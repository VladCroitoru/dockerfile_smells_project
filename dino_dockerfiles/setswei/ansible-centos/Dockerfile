# Select Source Centos OS
FROM centos

# Author
MAINTAINER setswei <kyle.hartigan@cybercrysis.net.au>

# Import RPM Keys
RUN rpm --import http://mirror.centos.org/centos/7/os/x86_64/RPM-GPG-KEY-CentOS-7 && \
    rpm --import http://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-7 && \
    yum update -y && \
    yum clean all && \

    # Download and Install EPEL
    yum -y install epel-release && \

    # Update Yum
    yum -y update && \

    # Install Ansible
    yum -y install ansible && \

    # Yum Clean up
    yum clean all && \

    # Create Ansible Inventory File
    echo "[local]\nlocalhost ansible_connection=local" > /etc/ansible/hosts