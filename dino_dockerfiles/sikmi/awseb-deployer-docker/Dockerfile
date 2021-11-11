FROM python:2.7.13

RUN apt-get update && \
    apt-get install -y zip \
                    unzip \
                    jq \
                    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

RUN pip install awsebcli \
                awscli

ENV DOCKER_VERSION=17.03.0-ce
RUN curl -L -o /tmp/docker-${DOCKER_VERSION}.tgz https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz && \
    tar -xz -C /tmp -f /tmp/docker-${DOCKER_VERSION}.tgz && \
    mv /tmp/docker/* /usr/bin

RUN curl https://raw.githubusercontent.com/apex/apex/master/install.sh | sh

ENV TERRAFORM_VERSION 0.9.6
RUN curl -L -o /tmp/terraform-${TERRAFORM_VERSION}.zip "https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip" && \
    unzip /tmp/terraform-${TERRAFORM_VERSION}.zip -d /bin && \
    rm -rf /tmp/terraform*
