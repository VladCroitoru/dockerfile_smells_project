FROM ubuntu:latest
MAINTAINER Rodney Hawkins

RUN apt-get update && apt-get install -y -qq --no-install-recommends curl \
    python \
    openssh-client \
    python-openssl \
    python-pip \
    python-setuptools \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common \
    ansible \
    ruby-dev \
    build-essential

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y nodejs

# Install gcloud-sdk and kubectl
ENV HOME /
RUN curl https://sdk.cloud.google.com | bash
ENV PATH /google-cloud-sdk/bin:$PATH
RUN gcloud components install kubectl

# Install Docker
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
RUN add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
RUN apt-get update && apt-get install -y docker-ce
RUN apt-get clean && rm -rf /var/lib/apt-lists/*

# Install Tooling
RUN gem install kubernetes-deploy

RUN pip install docker-compose

CMD ["/bin/bash"]
