# ========================================
# CREATE UPDATED BASE IMAGE
# ========================================

FROM debian:bullseye-slim AS base

RUN apt-get update \
    && apt-get dist-upgrade -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# ========================================
# GENERAL PREREQUISITES
# ========================================

FROM base

RUN apt-get update \
    && apt-get install -y curl unzip git bash-completion jq ssh sudo gnupg groff \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Adding  GitHub public SSH key to known hosts
RUN ssh -T -o "StrictHostKeyChecking no" -o "PubkeyAuthentication no" git@github.com || true

# ========================================
# COPY FILES
# ========================================

ADD src /

# # ========================================
# # PYTHON
# # ========================================

# RUN apt-get update \
#     && apt-get install -y python python-pip python3 python3-pip \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*

# ========================================
# AWS CLI
# ========================================

ENV AWS_CLI_VERSION=2.2.43

RUN curl https://awscli.amazonaws.com/awscli-exe-linux-x86_64-${AWS_CLI_VERSION}.zip -o awscliv2.zip \
    && curl https://awscli.amazonaws.com/awscli-exe-linux-x86_64-${AWS_CLI_VERSION}.zip.sig  -o awscliv2.sig \
    && gpg --import aws-cli.asc \
    && gpg --verify awscliv2.sig awscliv2.zip \
    && unzip awscliv2.zip \
    && ./aws/install \
    && rm -rf ./aws \
    && rm -f awscliv2.zip aws-cli.asc awscliv2.sig

ENV AWS_PAGER=""


# ========================================
# TERRAFORM
# ========================================

ENV TERRAFORM_VERSION=1.0.8

RUN curl -Os https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
    && curl -Os https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_SHA256SUMS \
    && curl -Os https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_SHA256SUMS.sig \
    && gpg --import hashicorp.asc \
    && gpg --verify terraform_${TERRAFORM_VERSION}_SHA256SUMS.sig terraform_${TERRAFORM_VERSION}_SHA256SUMS \
    && grep terraform_${TERRAFORM_VERSION}_linux_amd64.zip terraform_${TERRAFORM_VERSION}_SHA256SUMS > terraform_${TERRAFORM_VERSION}_SHA256SUM \
    && shasum -a 256 -c terraform_${TERRAFORM_VERSION}_SHA256SUM \
    && unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
    && rm -f terraform_${TERRAFORM_VERSION}_* hashicorp.asc \
    && mv terraform /usr/local/bin/ \
    && terraform -install-autocomplete


# ========================================
# TERRAGRUNT
# ========================================

ENV TERRAGRUNT_VERSION=0.33.2

RUN curl -L https://github.com/gruntwork-io/terragrunt/releases/download/v${TERRAGRUNT_VERSION}/terragrunt_linux_amd64 -o terragrunt \
    && chmod +x terragrunt \
    && mv terragrunt /usr/local/bin/


# ========================================
# KUBECTL
# ========================================


ENV KUBECTL_VERSION=1.21.5

RUN curl -L https://storage.googleapis.com/kubernetes-release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl -o kubectl \
    && curl -Os https://storage.googleapis.com/kubernetes-release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl.sha256 \
    && bash -c 'echo "$(<kubectl.sha256) kubectl" | sha256sum --check' \
    && chmod +x kubectl \
    && mv kubectl /usr/local/bin/ \
    && rm -f kubectl.sha256

# ========================================
# KUBECTL CROSSPLANE PLUGIN
# ========================================

ENV CROSSPLANE_VERSION=v1.4.1

RUN curl -sL https://raw.githubusercontent.com/crossplane/crossplane/master/install.sh | CHANNEL=stable VERSION=${CROSSPLANE_VERSION} sh \
    && mv kubectl-crossplane /usr/local/bin


# ========================================
# HELM
# ========================================

ENV HELM_VERSION=3.7.0

RUN curl -L https://get.helm.sh/helm-v${HELM_VERSION}-linux-amd64.tar.gz -o helm.tgz \
    && tar -zxvf helm.tgz \
    && rm helm.tgz \
    && mv linux-amd64/helm /usr/local/bin/ \
    && rm -R linux-amd64 \
    && echo "source <(helm completion bash)" >> ~/.bashrc


# ========================================
# AWS IAM AUTHENTICATOR
# ========================================

ENV AWSIAMAUTH_VERSION=1.21.2/2021-07-05

RUN curl -L https://amazon-eks.s3-us-west-2.amazonaws.com/${AWSIAMAUTH_VERSION}/bin/linux/amd64/aws-iam-authenticator -o aws-iam-authenticator \
    && chmod +x aws-iam-authenticator \
    && mv aws-iam-authenticator /usr/local/bin/


# ========================================
# SAML2AWS
# ========================================

# ENV SAML2AWS_VERSION=2.13.0

# RUN curl -L "https://github.com/Versent/saml2aws/releases/download/v${SAML2AWS_VERSION}/saml2aws_${SAML2AWS_VERSION}_linux_amd64.tar.gz" -o saml2aws.tar.gz \
#     && tar -zxvf saml2aws.tar.gz \
#     && rm saml2aws.tar.gz \
#     && mv saml2aws /usr/local/bin/


# ========================================
# KAFKA MESSAGE PRODUCER
# ========================================

RUN apt-get update \
    && apt-get install -y kafkacat \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# ========================================
# END
# ========================================

CMD [ "bash" ]

# ========================================
# ISSUES
# ========================================

# debconf: unable to initialize frontend: Dialog
# debconf: (TERM is not set, so the dialog frontend is not usable.)
# debconf: falling back to frontend: Readline
# debconf: unable to initialize frontend: Readline
# debconf: (Can't locate Term/ReadLine.pm in @INC (you may need to install the Term::ReadLine module) (@INC contains: /etc/perl /usr/local/lib/x86_64-linux-gnu/perl/5.24.1 /usr/local/share/perl/5.24.1 /usr/lib/x86_64-linux-gnu/perl5/5.24 /usr/share/perl5 /usr/lib/x86_64-linux-gnu/perl/5.24 /usr/share/perl/5.24 /usr/local/lib/site_perl /usr/lib/x86_64-linux-gnu/perl-base .) at /usr/share/perl5/Debconf/FrontEnd/Readline.pm line 7, <> line 3.)
# debconf: falling back to frontend: Teletype
# dpkg-preconfigure: unable to re-open stdin:
