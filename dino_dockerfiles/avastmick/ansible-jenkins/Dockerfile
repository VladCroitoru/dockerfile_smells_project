FROM jenkins:latest

# This creates a full Build machine that will:
#   - be based on Ubuntu latest
#   - have Jenkins 1.6+ installed
#   - have Ansible installed
#   - have Vagrant installed to manage virtual machine images
#   - have Packer installed to create and maintain VM images from ISOs
#   - have Git installed
#   - have any other tools required for automated builds
#### Derived image, the base of which is in a non-root user, so revert
USER root

#### Build variables
ARG PACKER_VERSION=0.10.0
#### Repository URL
ARG GITHUB_URL=github.com

#### Build variables
ENV ANSIBLE_HOME /home/ansible

#### Open ports to be used
# for main Jenkins web interface:
EXPOSE 8080 8090
# will be used by attached slave agents (note latter unlikely to be used):
EXPOSE 50000 50001
# Other ports

#### Users and groups
# Create user
ARG ansible_user=ansible
ARG ansible_group=ansible
ARG ansible_uid=1001
ARG ansible_gid=1001

#### Installation
## Install via apt
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        apt-utils \
        build-essential \
        ca-certificates curl \
        debconf-utils \
        file \
        git \
        libffi-dev libxslt1-dev libssl-dev libxml2-dev libkrb5-dev \
        openssl \
        python python-dev python-pip python-setuptools \
        sudo uuid-dev unzip wget && \
    apt-get clean

# Install Ansible and dependencies (via pip) forcing the deps to latest
RUN pip install --upgrade pip setuptools wheel
RUN pip install ansible kerberos pywinrm  requests_kerberos xmltodict

# Install Packer binary
RUN curl -sf -O https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip && \
    unzip packer_${PACKER_VERSION}_linux_amd64.zip -d /usr/bin

# Install Vagrant
RUN apt-get update && \
    apt-get install --no-install-recommends -y vagrant

######### Configure
# Ensure that the Jenkins jobs can interact with the GitHub Enterprise server
RUN echo | openssl s_client -showcerts -connect ${GITHUB_URL}:443 2>&1 | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > /etc/ssl/certs/ca-certificates.crt

## Other
RUN groupadd -g ${ansible_gid} ${ansible_group} \
    && useradd -d "$ANSIBLE_HOME" -u ${ansible_uid} -g ${ansible_gid} -m -s /bin/bash ${ansible_user} \
    # Add jenkins and ansible to sudoers with no password
    && echo "jenkins        ALL=(ALL)       NOPASSWD: ALL" > /etc/sudoers.d/jenkins \
    && echo "ansible        ALL=(ALL)       NOPASSWD: ALL" > /etc/sudoers.d/ansible

# ADD [external_file] [/local_dir/external_file]
# Ansible configuration
COPY ansible.cfg /etc/ansible/.

#### Set user and run following as user
USER jenkins

# Add Jenkins plugins
COPY jenkins/plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/ref/plugins.txt

# Add Jenkins JOBS - MUST be after loading plugins
COPY jenkins/jobs /usr/share/jenkins/ref/jobs

#### Volumes - this MUST be AFTER all material changes - i.e. changes that affect disk, but BEFORE any exec processes
# Jenkins home directory is a volume, so configuration and build history
# can be persisted and survive image upgrades - not required given this is a derived image
# VOLUME ${JENKINS_HOME}

#### LEAVE EVERYTHING BELOW THIS LINE #########################
