FROM ubuntu:16.04
MAINTAINER Rafal Leszko

RUN apt-get update

# Let's start with some basic stuff.
RUN apt-get install -qqy \
    apt-transport-https \
    ca-certificates \
    curl \
    lxc \
    iptables

# Install Docker from Docker Inc. repositories.
RUN curl -sSL https://get.docker.com/ | sh

# Define additional metadata for our image.
VOLUME /var/lib/docker

# Install Docker Compose
RUN apt-get install -y python-pip
RUN pip install docker-compose

# SSHD setup for jenkins-slave 
RUN locale-gen en_US.UTF-8 &&\
    apt-get -q update &&\
    DEBIAN_FRONTEND="noninteractive" apt-get -q upgrade -y -o Dpkg::Options::="--force-confnew" --no-install-recommends &&\
    DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--force-confnew"  --no-install-recommends openssh-server &&\
    apt-get -q autoremove &&\
    apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin &&\
    sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd &&\
    mkdir -p /var/run/sshd
ENV LANG en_US.UTF-8 ENV LANGUAGE en_US:en ENV LC_ALL en_US.UTF-8 

# Install JDK 8
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk

# Install Ansible
RUN apt-get install -y software-properties-common && \
    apt-add-repository ppa:ansible/ansible && \
    apt-get update && \
    apt-get install -y ansible
ADD ./resources/ansible.cfg /etc/ansible/ansible.cfg


# Set user jenkins to the image 
RUN useradd -m -d /home/jenkins -s /bin/sh jenkins && \
    echo "jenkins:jenkins" | chpasswd && \
    usermod -aG docker jenkins

# Standard SSH port 
EXPOSE 22  

# Install the magic wrapper.
RUN mv /usr/sbin/sshd /usr/sbin/sshd_real
ADD ./resources/wrapdocker /usr/sbin/sshd
RUN chmod +x /usr/sbin/sshd

CMD ["sshd"]
