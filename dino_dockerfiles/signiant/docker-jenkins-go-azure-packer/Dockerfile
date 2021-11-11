FROM signiant/docker-jenkins-centos-base:centos7-java8
MAINTAINER devops@signiant.com

# Set the timezone
RUN unlink /etc/localtime
RUN ln -s /usr/share/zoneinfo/America/New_York /etc/localtime

COPY yum-packages.list /tmp/yum.packages.list
RUN chmod +r /tmp/yum.packages.list && \
    yum update -y && \
    yum groupinstall -y "Development tools" && \
    yum install -y `cat /tmp/yum.packages.list`

# Install the latest version of git
RUN cd /tmp && \
    wget https://github.com/git/git/archive/v2.7.0.tar.gz && \
    tar xvfz ./v2.7.0.tar.gz && \
    cd git-2.7.0 && \
    make configure && \
    ./configure --prefix=/usr && \
    make && \
    make install

# Install Python 2.7.X for Umpire
RUN cd /tmp && \
    wget https://www.python.org/ftp/python/2.7.11/Python-2.7.11.tgz && \
    tar xvfz Python-2.7.11.tgz && \
    cd Python-2.7.11 && \
    ./configure --prefix=/usr/local && \
    make && \
    make altinstall

# Install pip
RUN cd /tmp && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    python2.7 ./get-pip.py

# Install PIP packages
COPY pip.packages.list /tmp/pip.packages.list
RUN chmod +r /tmp/pip.packages.list && \
    /bin/bash -l -c "pip2.7 install `cat /tmp/pip.packages.list | tr \"\\n\" \" \"`"

# install azure-cli
RUN npm install azure-cli -g

RUN wget https://releases.hashicorp.com/packer/0.9.0/packer_0.9.0_linux_amd64.zip

RUN mkdir /usr/local/bin/packer
RUN mkdir /home/bldmgr/goworkspace

RUN unzip packer_0.9.0_linux_amd64.zip -d /usr/local/bin/packer

RUN wget https://storage.googleapis.com/golang/go1.5.3.linux-amd64.tar.gz -O /tmp/go1.5.3.linux-amd64.tar.gz
RUN tar -C /usr/local -xzf /tmp/go1.5.3.linux-amd64.tar.gz
RUN ls /usr/local/go

ENV GOROOT=/usr/local/go
ENV GOBIN=/usr/local/bin/packer
ENV GOPATH=/home/bldmgr/goworkspace
ENV GO15VENDOREXPERIMENT=1
RUN export PATH=$PATH:/usr/local/go/bin

#now an official builder so don't need plugin
#RUN /usr/local/go/bin/go get github.com/Azure/packer-azure/packer/plugin/packer-builder-azure-arm
RUN /usr/local/go/bin/go get github.com/Azure/packer-azure/packer/plugin/packer-provisioner-azure-custom-script-extension

# Make sure anything/everything we put in the build user's home dir is owned correctly
RUN chown -R $BUILD_USER:$BUILD_USER_GROUP /home/$BUILD_USER

EXPOSE 22

# This entry will either run this container as a jenkins slave or just start SSHD
# If we're using the slave-on-demand, we start with SSH (the default)

# Default Jenkins Slave Name
ENV SLAVE_ID JAVA_NODE
ENV SLAVE_OS Linux

ADD start.sh /
RUN chmod 777 /start.sh
