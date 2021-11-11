# https://github.com/developertown/vsts-agent
# FROM developertown/vsts-agent
FROM microsoft/vsts-agent:ubuntu-16.04-tfs-2017-docker-17.06.0-ce-standard

RUN apt-get update -qq && \
    apt-get install -y \
      wget \
      make \
      python3.5 \
      python3-pip

# Install awscli
RUN pip3 install awscli --upgrade

# Install golang
# - Required for the Amazon ECR Credential Helper
RUN wget https://storage.googleapis.com/golang/go1.8.1.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go1.8.1.linux-amd64.tar.gz

ENV GOPATH=/usr/local/go/bin
ENV PATH=$PATH:/usr/local/go/bin

# Install Amazon ECR Credential Helper
#  - For the AWS Container Registry
RUN cd /usr/local/go/bin && \
    mkdir -p src/github.com/awslabs/ && \
    mkdir -p local && \
    cd src/github.com/awslabs/ && \
    git clone https://github.com/awslabs/amazon-ecr-credential-helper.git && \
    cd amazon-ecr-credential-helper && \
    make && \
    mv ./bin/local/docker-credential-ecr-login /usr/local/go/bin/local/


ENV PATH=$PATH:/usr/local/go/bin/local/

# Install kubectl
# - For Deployments
RUN curl \
  -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl && \
  chmod +x ./kubectl && \
  mv ./kubectl /usr/local/bin/kubectl && \
  crontab -l | { cat; echo "@monthly docker system prune -f --volumes"; } | crontab -


RUN mkdir ~/.docker && echo '{"credsStore": "ecr-login"}' >> ~/.docker/config.json
