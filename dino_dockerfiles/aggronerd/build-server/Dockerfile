# Base on latest LTS
FROM ubuntu:14.04
MAINTAINER Gregory Doran <greg@gregorydoran.co.uk>

# Install general stuff
RUN apt-get update
RUN apt-get install -y openssh-server curl openjdk-7-jdk unzip
RUN mkdir /var/run/sshd
RUN adduser --quiet jenkins
RUN sudo -u jenkins mkdir /home/jenkins/.ssh
RUN sudo -u jenkins mkdir /home/jenkins/workspace
COPY key.pub /home/jenkins/.ssh/authorized_keys
COPY entrypoint.sh /entrypoint.sh

# Sudo for Jenkins
RUN echo "jenkins ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Install RVM
RUN sudo -u jenkins bash -c "HOME=/home/jenkins gpg --keyserver keyserver.ubuntu.com --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3; curl -sSL https://get.rvm.io | HOME=/home/jenkins bash -s stable"

# Install NodeJS
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -
RUN apt-get install -y nodejs

# Install bower
RUN npm install -g bower

# Install grunt
RUN npm install -g grunt-cli

# Install AWS cli
RUN apt-get install -y python-pip
RUN pip install awscli

# Install git
RUN apt-get install -y git

# Install packer
RUN wget https://releases.hashicorp.com/packer/0.10.0/packer_0.10.0_linux_amd64.zip -O temp.zip && unzip -d /usr/bin temp.zip && rm temp.zip

# General building tools
RUN apt-get install -y libxml2-dev libxslt1-dev zlib1g-dev libmysqlclient-dev libsqlite3-dev libgmp-dev

# Install PhantomJS
RUN apt-get install -y phantomjs

# Install postgres client
RUN apt-get install -y postgresql-client libpq-dev

# Install mysql client
RUN apt-get install -y mysql-client

# Install python
RUN apt-get install -y python python-pip

# Install boto
RUN pip install boto3

# Copy SSH config
COPY ssh_config /home/jenkins/.ssh/config
COPY ssh_known_hosts /home/jenkins/.ssh/known_hosts
RUN chown jenkins:jenkins /home/jenkins/.ssh/*

EXPOSE 22
CMD ["/entrypoint.sh"]
