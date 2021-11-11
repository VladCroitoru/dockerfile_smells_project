# This file can build a jenkis-slave with node, docker and python env.
FROM debian:jessie

# Update packages
RUN apt-get update && apt-get -y upgrade

# prepare docker repo
RUN apt-get install -y apt-transport-https ca-certificates \
    && apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D \
    && touch /etc/apt/sources.list.d/docker.list \
    && echo 'deb https://apt.dockerproject.org/repo debian-jessie main' >> /etc/apt/sources.list.d/docker.list

# Add user "jenkins" with password "jenkins"
RUN adduser --quiet jenkins && echo "jenkins:jenkins" | chpasswd
    
# install docker engine and start daemon, add jenkins user to docker group
RUN apt-get update \ 
    && apt-get install -y docker-engine \
    && gpasswd -a jenkins docker
    
# install nodejs via nvm
RUN apt-get install -y build-essential libssl-dev curl \
    && curl https://raw.githubusercontent.com/creationix/nvm/v0.31.0/install.sh | bash
RUN /root/.nvm/nvm.sh install stable \
    && /root/.nvm/nvm.sh use stable

# install python
RUN apt-get install -y python python3

# Add backports
RUN echo "deb http://http.debian.net/debian jessie-backports main" >> /etc/apt/sources.list && apt-get update

# Install java
RUN apt-get -t jessie-backports install -y openjdk-8-jdk

# Install Git and OpenSSH
RUN apt-get install -y git openssh-server && mkdir /var/run/sshd

ENV CI=true
EXPOSE 22

ADD entrypoint.sh /tmp/
RUN chmod +x /tmp/entrypoint.sh

ENTRYPOINT ["/tmp/entrypoint.sh"]
