FROM ubuntu:latest

# Make sure the package repository is up to date. please rebuild

ARG http_proxy
ARG https_proxy
ARG no_proxy

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y git openssh-server dos2unix unzip curl
# Install a basic SSH server
RUN apt-get install -y
RUN sed -i 's|session    required     pam_loginuid.so|session    optional     pam_loginuid.so|g' /etc/pam.d/sshd
RUN mkdir -p /var/run/sshd

# USER root

# Add user jenkins to the image
RUN adduser --quiet jenkins
# Set password for the jenkins user (you may want to alter this).
RUN echo "jenkins:jenkins" | chpasswd

RUN mkdir /home/jenkins/.m2
# ADD settings.xml /home/jenkins/.m2/
RUN chown -R jenkins:jenkins /home/jenkins/.m2/



# Install Terraform 0.13
ENV TF_VERSION="0.13.5"
ENV TF_BASE_URL="https://releases.hashicorp.com/terraform" \
    TF_FILE_NAME="terraform_${TF_VERSION}_linux_amd64.zip" \
    TF_CHECKSUM_FILE_NAME="terraform_${TF_VERSION}_SHA256SUMS" \
    TF_PLUGIN_CACHE_DIR="/var/cache/terraform"

RUN echo "Downloading Terraform from: ${TF_BASE_URL}/${TF_VERSION}/${TF_FILE_NAME}" \
    && curl -fOL ${TF_BASE_URL}/${TF_VERSION}/${TF_FILE_NAME} \
    && curl -fOL ${TF_BASE_URL}/${TF_VERSION}/${TF_CHECKSUM_FILE_NAME} \
    && sha256sum --ignore-missing -c ${TF_CHECKSUM_FILE_NAME} \
    && unzip ${TF_FILE_NAME} -d /tmp \
    && mv /tmp/terraform /usr/bin/terraform \
    && rm -f ${TF_FILE_NAME} ${TF_CHECKSUM_FILE_NAME} \
    && mkdir -p ${TF_PLUGIN_CACHE_DIR} && chmod 1777 ${TF_PLUGIN_CACHE_DIR} \
    && terraform --version

# Install TFLint

ENV TFLINT_VERSION="v0.20.2"
ENV TFLINT_BASE_URL="https://github.com/terraform-linters/tflint/releases/download" \
    TFLINT_FILE_NAME="tflint_linux_amd64.zip" \
    TFLINT_CHECKSUM_FILE_NAME="checksums.txt"

RUN echo "Downloading TFLint from: ${TFLINT_BASE_URL}/${TFLINT_VERSION}/${TFLINT_FILE_NAME}" \
    && curl -fOL ${TFLINT_BASE_URL}/${TFLINT_VERSION}/${TFLINT_FILE_NAME} \
    && curl -fOL ${TFLINT_BASE_URL}/${TFLINT_VERSION}/${TFLINT_CHECKSUM_FILE_NAME} \
    && curl -fOL ${TFLINT_BASE_URL}/${TFLINT_VERSION}/${TFLINT_CHECKSUM_FILE_NAME}.sig \
    && sha256sum --ignore-missing -c ${TFLINT_CHECKSUM_FILE_NAME} \
    && unzip ${TFLINT_FILE_NAME} -d /usr/bin/ \
    && rm -f ${TFLINT_FILE_NAME} ${TFLINT_CHECKSUM_FILE_NAME} \
    && tflint --version

# Install kubectl
# find the latest stable version via: curl https://storage.googleapis.com/kubernetes-release/release/stable.txt
ENV KUBECTL_VERSION="v1.19.2" \
    KUBECTL_CHECKSUM="f51adfe7968ee173dbfb3dabfc10dc774983cbf8a3a7c1c75a1423b91fda6821"
RUN curl -L https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl -o /tmp/kubectl && \
    echo "${KUBECTL_CHECKSUM}  /tmp/kubectl" | sha256sum -c - && \
    mv /tmp/kubectl /usr/bin/kubectl && \
    chmod 0755 /usr/bin/kubectl

# Install AWS cli tool
ENV AWS_CLI_VERSION=1.18.149
RUN apt-get install -y python3 python3-pip \
    && pip3 --no-cache-dir install \
    awscli==${AWS_CLI_VERSION}

# Install aws-iam-authenticator
ENV AWS_IAM_AUTHENTICATOR_VERSION="1.17.9/2020-08-04" \
    AWS_IAM_AUTHENTICATOR_CHECKSUM="fe958eff955bea1499015b45dc53392a33f737630efd841cd574559cc0f41800"
RUN curl -L https://amazon-eks.s3.amazonaws.com/${AWS_IAM_AUTHENTICATOR_VERSION}/bin/linux/amd64/aws-iam-authenticator \
        -o /tmp/aws-iam-authenticator && \
    echo "${AWS_IAM_AUTHENTICATOR_CHECKSUM}  /tmp/aws-iam-authenticator" | sha256sum -c - && \
    mv /tmp/aws-iam-authenticator /usr/bin/aws-iam-authenticator && \
    chmod 0755 /usr/bin/aws-iam-authenticator && \
    aws-iam-authenticator version

# Install amazon-ecr-credential-helper-releases
ENV AMAZON_ECR_CREDENTIAL_HELPER_VERSION="0.4.0" \
    AMAZON_ECR_CREDENTIAL_HELPER_CHECKSUM="2c8fc418fe1b5195388608c1cfb99ba008645f3f1beb312772c9490c39aa5904"
RUN curl -L https://amazon-ecr-credential-helper-releases.s3.amazonaws.com/${AMAZON_ECR_CREDENTIAL_HELPER_VERSION}/linux-amd64/docker-credential-ecr-login \
        -o /tmp/docker-credential-ecr-login && \
    echo "${AMAZON_ECR_CREDENTIAL_HELPER_CHECKSUM}  /tmp/docker-credential-ecr-login" | sha256sum -c - && \
    mv /tmp/docker-credential-ecr-login /usr/bin/docker-credential-ecr-login && \
    chmod 0755 /usr/bin/docker-credential-ecr-login && \
    docker-credential-ecr-login version

# Install helm 3
ENV HELM_VERSION=3.4.0
ENV HELM_BASE_URL="https://get.helm.sh"
ENV HELM_TAR_FILE="helm-v${HELM_VERSION}-linux-amd64.tar.gz"

RUN curl -L ${HELM_BASE_URL}/${HELM_TAR_FILE} | tar xvz && \
    mv linux-amd64/helm /usr/bin/helm && \
    chmod +x /usr/bin/helm && \
    rm -rf linux-amd64 && \
    helm version
    
# Install github cli
#https://github.com/cli/cli/releases/download/v1.3.1/gh_1.3.1_linux_amd64.tar.gz
ENV GITHUB_VERSION=1.3.1
ENV GITHUB_BASE_URL="https://github.com/cli/cli/releases/download/v${GITHUB_VERSION}"
ENV GITHUB_TAR_FILE="gh_${GITHUB_VERSION}_linux_amd64.tar.gz"

RUN curl -L ${GITHUB_BASE_URL}/${GITHUB_TAR_FILE} | tar xvz && \
    mv gh_${GITHUB_VERSION}_linux_amd64/bin/gh /usr/bin/gh && \
    chmod +x /usr/bin/gh && \
    rm -rf linux-amd64 && \
    gh version

# Install java 8
RUN apt-get install -y openjdk-8-jre-headless

# Install skopeo for Docker image magics
# RUN apt-get install -y skopeo

# Standard SSH port
EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
