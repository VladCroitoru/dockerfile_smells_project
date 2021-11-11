FROM jenkins/jenkins:lts
MAINTAINER Chris Gibson <git@twoitguys.com>

USER root

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install git && \
    apt-get clean && \
    rm -rf /var/cache/apt/* && \
    rm -rf /var/lib/apt/lists/* 

RUN wget https://releases.hashicorp.com/packer/1.2.0/packer_1.2.0_linux_amd64.zip
RUN unzip packer_1.2.0_linux_amd64.zip
RUN mv packer /usr/local/bin/
RUN chmod 0755 /usr/local/bin/packer
RUN wget https://releases.hashicorp.com/terraform/0.11.3/terraform_0.11.3_linux_amd64.zip
RUN unzip terraform_0.11.3_linux_amd64.zip
RUN mv terraform /usr/local/bin/
RUN chmod 0755 /usr/local/bin/terraform
RUN wget https://s3.amazonaws.com/aws-cli/awscli-bundle.zip
RUN unzip awscli-bundle.zip
RUN ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws
RUN rm packer_1.2.0_linux_amd64.zip
RUN rm terraform_0.11.3_linux_amd64.zip
RUN rm awscli-bundle.zip

USER jenkins
