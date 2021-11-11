FROM alpine:3.7

# Script is a combination of code from Dockerfiles of other images.
LABEL description="Docker image for Gitlab CI containing Terraform, KOPS, Kubectl and awscli" \
      maintainer="Vlaszaty <vlaszaty@gmail.com>"



# Install Terraform, as seen in https://github.com/djerfy/gitlab-ci-terraform
ENV TERRAFORM_VERSION=0.11.7
ENV TERRAFORM_FILENAME=terraform_${TERRAFORM_VERSION}_linux_amd64.zip
ENV TERRAFORM_BASEURL=https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}

RUN apk add --update git bash wget

RUN wget -q ${TERRAFORM_BASEURL}/${TERRAFORM_FILENAME} && \
    wget -qO- ${TERRAFORM_BASEURL}/terraform_${TERRAFORM_VERSION}_SHA256SUMS | grep "terraform_${TERRAFORM_VERSION}_linux_amd64.zip" | awk '{print $1}' > ${TERRAFORM_FILENAME}.sha256sum

RUN echo "$(cat ${TERRAFORM_FILENAME}.sha256sum)  ${TERRAFORM_FILENAME}" | sha256sum -c && \
    unzip ${TERRAFORM_FILENAME} -d /bin && \
    rm -f ${TERRAFORM_FILENAME}

# Install KOPS and Kubectl, as seen in https://github.com/AirHelp/docker-kops

# Kops version
ENV KOPS_VERSION=1.9.0
# https://kubernetes.io/docs/tasks/kubectl/install/
# latest stable kubectl: curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt
ENV KUBECTL_VERSION=v1.10.0

RUN apk --no-cache add ca-certificates \
  && apk --no-cache add --virtual build-dependencies curl \
  && curl -O --location --silent --show-error https://github.com/kubernetes/kops/releases/download/${KOPS_VERSION}/kops-linux-amd64 \
  && mv kops-linux-amd64 /usr/local/bin/kops \
  && curl -LO https://storage.googleapis.com/kubernetes-release/release/$KUBECTL_VERSION/bin/linux/amd64/kubectl \
  && mv kubectl /usr/local/bin/kubectl \
  && chmod +x /usr/local/bin/kops /usr/local/bin/kubectl \
  && apk del --purge build-dependencies

# Install awscli using pip, as seen in https://github.com/anigeo/docker-awscli
RUN 	mkdir -p /aws && \
	apk -Uuv add groff less python py-pip && \
  pip install --upgrade pip && \
	pip install awscli && \
	apk --purge -v del py-pip && \
	rm /var/cache/apk/*
