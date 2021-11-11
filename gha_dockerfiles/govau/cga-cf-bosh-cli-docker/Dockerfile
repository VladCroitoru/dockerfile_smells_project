FROM ubuntu:18.04

# Install base packages, ansible, nodejs
RUN apt-get update && DEBIAN_FRONTEND="noninteractive" apt-get -y install \
    awscli \
    curl \
    dnsutils \
    gcc \
    git \
    jq \
    software-properties-common \
    zip \
    unzip \
    wget \
    python-boto3 && \
    apt-add-repository ppa:ansible/ansible && \
    apt-get update && apt-get -y install \
    ansible && \
    bash -o pipefail -c "curl -L https://deb.nodesource.com/setup_8.x | bash" && \
    apt-get -y install \
    nodejs && \
    rm -rf /var/lib/apt/lists/*

# Install bosh-cli
RUN curl -L https://s3.amazonaws.com/bosh-cli-artifacts/bosh-cli-2.0.48-linux-amd64 > /usr/local/bin/bosh && \
    chmod a+x /usr/local/bin/bosh

# Install credhub-cli
RUN bash -o pipefail -c "curl -L https://github.com/cloudfoundry-incubator/credhub-cli/releases/download/2.9.0/credhub-linux-2.9.0.tgz | tar -xz -C /usr/local/bin"

# Install go
RUN bash -o pipefail -c "curl -L https://storage.googleapis.com/golang/go1.14.15.linux-amd64.tar.gz | tar -xz -C /usr/local"

# Set Go environment variables
ENV GOROOT=/usr/local/go GOPATH=/go PATH=/go/bin:/usr/local/go/bin:$PATH

# Install glide
RUN mkdir -p /go/bin && \
    bash -o pipefail -c "curl -L https://github.com/Masterminds/glide/releases/download/v0.13.3/glide-v0.13.3-linux-amd64.tar.gz | tar -xz linux-amd64/glide" && \
    mv linux-amd64/glide /go/bin && \
    rm -rf linux-amd64

# Install go tools
RUN go get \
    github.com/golang/dep/cmd/dep \
    github.com/GeertJohan/fgt \
    golang.org/x/lint/golint \
    github.com/golang/protobuf/protoc-gen-go \
    github.com/govau/le-dns-certs/cmd/route53renewer \
    github.com/govau/sdget \
    github.com/jteeuwen/go-bindata/... \
    golang.org/x/tools/cmd/cover \
    github.com/cespare/xxhash \
    github.com/prometheus/alertmanager/cmd/amtool

# Install common NPM stuff:
RUN cd $(npm root -g)/npm && \
    npm install fs-extra && \
    npm install -g yarn

# Install terraform
ENV TERRAFORM_VERSION "0.12.30"
RUN curl -L https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip > /tmp/terraform.zip && \
    unzip /tmp/terraform.zip terraform -d /usr/local/bin && \
    rm /tmp/terraform.zip

RUN curl -L https://github.com/google/protobuf/releases/download/v3.5.1/protoc-3.5.1-linux-x86_64.zip > /tmp/protoc.zip && \
    unzip /tmp/protoc.zip -d /usr/local && \
    rm /tmp/protoc.zip

# Install cloudfoundry terraform provider
ENV CLOUDFOUNDRY_VERSION "0.14.2"
RUN mkdir -p /root/.terraform.d/plugins/linux_amd64 && \
    curl -L https://github.com/cloudfoundry-community/terraform-provider-cloudfoundry/releases/download/v${CLOUDFOUNDRY_VERSION}/terraform-provider-cloudfoundry_${CLOUDFOUNDRY_VERSION}_linux_amd64.zip > /tmp/terraform-provider-cloudfoundry_linux_amd64.zip && \
    unzip -p /tmp/terraform-provider-cloudfoundry_linux_amd64.zip terraform-provider-cloudfoundry_v0.14.2 > /root/.terraform.d/plugins/linux_amd64/terraform-provider-cloudfoundry && \
    chmod a+x /root/.terraform.d/plugins/linux_amd64/terraform-provider-cloudfoundry && \
    rm /tmp/terraform-provider-cloudfoundry_linux_amd64.zip

# Install kubectl
RUN curl -L https://storage.googleapis.com/kubernetes-release/release/v1.13.2/bin/linux/amd64/kubectl > /usr/local/bin/kubectl && \
    chmod a+x /usr/local/bin/kubectl

# Install helm
# RUN bash -o pipefail -c "curl -L https://storage.googleapis.com/kubernetes-helm/helm-v2.12.2-linux-amd64.tar.gz | tar -xz -C /usr/local/bin"
RUN curl -L https://get.helm.sh/helm-v2.12.2-linux-amd64.tar.gz > /tmp/helm.tar.gz && \
    mkdir /tmp/helm && \
    tar -xz -C /tmp/helm -f /tmp/helm.tar.gz && \
    mv /tmp/helm/linux-amd64/helm /tmp/helm/linux-amd64/tiller /usr/local/bin

# Install svcat
RUN curl -L https://download.svcat.sh/cli/v0.1.39/linux/amd64/svcat > /usr/local/bin/svcat && \
    chmod a+x /usr/local/bin/svcat

# Install chaostoolkit
RUN curl -L https://github.com/chaostoolkit/chaostoolkit-bundler/releases/download/2019.05.04/chaostoolkit-bundle_linux-amd64-2019.05.04 > /usr/local/bin/chaos && \
    chmod a+x /usr/local/bin/chaos
