FROM golang:alpine
MAINTAINER Nigel Gibbs <nigel@gibbsoft.com>


ENV TERRAFORM_VERSION=0.8.8
ENV TERRAGRUNT_VERSION=0.11.1
ENV TERRAFORM_CREDSTASH_VERSION=0.1.0
ENV TERRAGRUNT_TFPATH=/go/bin/terraform
ENV TF_DEV=1
ENV PATH=${PATH}:/go/bin

RUN apk add --update --no-cache build-base openssl-dev libffi-dev python2-dev openssh python2 py2-pip py-virtualenv zip git bash curl

RUN mkdir -p ${GOROOT} ${GOROOT}/bin ${GOBIN}

RUN curl -sL https://github.com/gruntwork-io/terragrunt/releases/download/v$TERRAGRUNT_VERSION/terragrunt_linux_386 \
  -o /bin/terragrunt && chmod +x /bin/terragrunt

WORKDIR $GOPATH/src/github.com/hashicorp/terraform
RUN git clone https://github.com/hashicorp/terraform.git ./ && \
    git checkout v${TERRAFORM_VERSION} && \
    /bin/bash scripts/build.sh

RUN go get -v -u github.com/sspinc/terraform-provider-credstash
WORKDIR $GOPATH/src/github.com/sspinc/terraform-provider-credstash
RUN git checkout v${TERRAFORM_CREDSTASH_VERSION} && \
    make build && \
    mv terraform-provider-credstash /go/bin/

RUN rm -rf $GOPATH/src

WORKDIR $GOPATH
