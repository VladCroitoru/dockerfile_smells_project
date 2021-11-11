FROM ubuntu:14.04

RUN apt-get update > /dev/null && \
    apt-get upgrade -y > /dev/null && \
    apt-get autoremove -y > /dev/null && \
    apt-get install -y \
      apt-transport-https \
      python-pip \
      python-dev \
      python-virtualenv \
      libffi-dev \
      libssl-dev \
      libldap2-dev \
      libmysqlclient-dev \
      libsasl2-dev \
      libxslt-dev \
      libxml2-dev \
      python-yaml \
      ca-certificates \
      openssh-client \
      vim \
      git \
      curl \
      wget \
      jq

# Install node 6.9.X (LTS)
RUN curl https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -
RUN echo 'deb https://deb.nodesource.com/node_6.x trusty main' > /etc/apt/sources.list.d/nodesource.list
RUN apt-get update > /dev/null && apt-get install nodejs

RUN pip install pip==9.0.1
RUN pip install virtualenv==15.1.0
RUN pip install aws
RUN pip install awscli==1.10.32

CMD lsb_release -a
