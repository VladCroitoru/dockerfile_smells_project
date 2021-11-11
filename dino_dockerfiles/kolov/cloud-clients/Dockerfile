FROM ubuntu:16.04

RUN apt-get update && \
    apt-get upgrade -y

RUN apt-get install --yes --force-yes apt-utils tzdata locales

# Set the timezone
RUN echo "Europe/Berlin" | tee /etc/timezone && \
    ln -fs /usr/share/zoneinfo/Europe/Berlin /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

# Set the locale for UTF-8 support
RUN echo en_US.UTF-8 UTF-8 >> /etc/locale.gen && \
    locale-gen && \
    update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# AWS CLI needs the PYTHONIOENCODING environment varialbe to handle UTF-8 correctly:
ENV PYTHONIOENCODING=UTF-8

# man and less are needed to view 'aws <command> help'
# ssh allows us to log in to new instances
# vim is useful to write shell scripts
# python* is needed to install aws cli using pip install

RUN apt-get install -y \
    less \
    man \
    ssh \
    python \
    python-pip \
    python-virtualenv \
    vim

RUN adduser --disabled-login --gecos '' aws
WORKDIR /home/aws

USER aws

RUN wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-188.0.1-linux-x86_64.tar.gz && \
    tar -xvf google-cloud-sdk-188.0.1-linux-x86_64.tar.gz && \
    ./google-cloud-sdk/install.sh

RUN \
    mkdir aws && \
    virtualenv aws/env && \
    ./aws/env/bin/pip install awscli traceback2 && \
    echo 'source $HOME/aws/env/bin/activate' >> .bashrc && \
    echo 'complete -C aws_completer aws' >> .bashrc

USER root

RUN apt-get install curl -y &&   \
    apt-get install gnupg2 -y && \
    apt-get install software-properties-common python-software-properties -y && \
    apt-get install apt-transport-https -y
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg |  apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
RUN apt-get update
RUN apt-get install -y docker-ce
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
RUN chmod +x ./kubectl && mv ./kubectl /usr/local/bin/kubectl

USER aws
RUN echo 123 > t && echo 123 |  gpg --no-tty --passphrase-fd 0 --symmetric > /dev/null

ENV PATH="/home/aws/google-cloud-sdk/bin:/home/aws/aws/env/bin:${PATH}"
