# Used to create docker image for running the commands invoked by the stubs in ../scripts/.

FROM centos:7.5.1804

ENV TERRAFORM_VERSION=0.8.8
ENV TERRAGRUNT_VERSION=v0.6.0
ENV DOCKER_COMPOSE_VERSION=1.9.0

ADD yum.repos.d/docker.repo /etc/yum.repos.d/
ADD ./requirements.txt /infra/requirements.txt

RUN yum install -y epel-release && \
    yum install -y bash ca-certificates curl docker-engine gawk git git openssl python-pip unzip wget && \
    cd /tmp && \
    curl -sSLO https://github.com/gruntwork-io/terragrunt/releases/download/${TERRAGRUNT_VERSION}/terragrunt_linux_amd64 && \
    mv terragrunt_linux_amd64 /usr/local/bin/terragrunt && \
    curl -sSLO https://releases.hashicorp.com/terraform/$TERRAFORM_VERSION/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    unzip terraform_*_linux_amd64.zip -d /usr/bin && \
    rm -rf /tmp/* && \
    rm -rf /var/tmp/* && \
    chmod 755 /usr/local/bin/terragrunt && \
    yum group install -y "Development Tools" && yum install -y python-devel && \
    pip install -r /infra/requirements.txt && \
    curl -L "https://github.com/docker/compose/releases/download/$DOCKER_COMPOSE_VERSION/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose && \
    yum group remove "Development Tools" -y && yum clean all

ADD . /infra
