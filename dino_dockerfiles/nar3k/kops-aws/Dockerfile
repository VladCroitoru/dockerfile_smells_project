FROM alpine:3.7

RUN apk update
RUN apk add git jq curl unzip wget python git jq unzip wget python docker
RUN curl https://s3.amazonaws.com/aws-cli/awscli-bundle.zip -o awscli-bundle.zip
RUN unzip awscli-bundle.zip
RUN ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws
RUN rm -rf awscli-bundle/ awscli-bundle.zip
ENV HUGO_VERSION="0.40.3"
RUN wget https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz
RUN tar -xf hugo_${HUGO_VERSION}_Linux-64bit.tar.gz
RUN chmod +x hugo
RUN mv hugo /usr/local/bin/hugo
RUN rm -rf hugo_${HUGO_VERSION}_Linux-64bit.tar.gz
ENV TERRAFORM_VERSION="0.11.7"
RUN wget https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
RUN unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip
RUN chmod +x terraform
RUN mv terraform /usr/local/bin/terraform
RUN rm -rf terraform_${TERRAFORM_VERSION}_linux_amd64.zip
ENV KUBECTL_VERSION="1.9.7"
RUN wget https://storage.googleapis.com/kubernetes-release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl
RUN chmod +x kubectl
RUN mv kubectl /usr/local/bin/kubectl
ENV KOPS_VERSION="1.9.0"
RUN wget https://github.com/kubernetes/kops/releases/download/${KOPS_VERSION}/kops-linux-amd64
RUN chmod +x kops-linux-amd64
RUN mv kops-linux-amd64 /usr/local/bin/kops
RUN mkdir /kops-aws
RUN mkdir ~/.ssh
RUN mkdir ~/.kube
WORKDIR /kops-aws
