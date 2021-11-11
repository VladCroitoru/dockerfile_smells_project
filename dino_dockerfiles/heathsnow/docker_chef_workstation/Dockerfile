FROM ubuntu:14.04

RUN \
  apt-get update && apt-get install -y \
    wget \
    vim \
    build-essential \
    unzip \
    groff \
    less \
    ca-certificates

# Install Packer (0.12.2)
RUN \
  mkdir /packer

RUN \
  cd /packer && \
  wget https://releases.hashicorp.com/packer/0.12.2/packer_0.12.2_linux_amd64.zip && \
  unzip packer_0.12.2_linux_amd64.zip && \
  rm packer_0.12.2_linux_amd64.zip

ENV PATH=$PATH:/packer/

# Install ChefDK
RUN \
  wget https://packages.chef.io/stable/ubuntu/14.04/chefdk_0.14.25-1_amd64.deb && \
  dpkg -i chefdk_0.14.25-1_amd64.deb && \
  rm chefdk_0.14.25-1_amd64.deb

ENV PATH="/root/.chefdk/gem/ruby/2.1.0/bin:$PATH"

# Install Terraform (0.8.7)
RUN \
  mkdir /terraform

RUN \
  cd /terraform && \
  wget https://releases.hashicorp.com/terraform/0.8.7/terraform_0.8.7_linux_amd64.zip && \
  unzip terraform_0.8.7_linux_amd64.zip && \
  rm terraform_0.8.7_linux_amd64.zip

ENV PATH=$PATH:/terraform/

# Executables PATH addition
ENV export PATH=~/bin:$PATH

# Install AWS CLI
RUN \
  wget https://s3.amazonaws.com/aws-cli/awscli-bundle.zip && \
  unzip awscli-bundle.zip && \
  /usr/bin/python3.4 ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \
  rm awscli-bundle.zip

# Install Bundler
RUN \
  chef gem install bundler

# Install Test Kitchen vSphere gem
RUN \
  chef gem install chef-provisioning-vsphere -v 0.9.0

RUN \
  locale-gen en_US.UTF-8

ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8

VOLUME ["/repo"]
WORKDIR /repo

CMD ["/bin/bash"]
