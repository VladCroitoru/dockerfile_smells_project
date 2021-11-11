FROM alpine:3.7
LABEL maintainer="Clemens Queissner <clemens.queissner@cq-design.de>"
LABEL description="This image provides a lightweight build and deployment platform for a Hugo generated sites.\
Include AWS cli tool and Terraform for deployment and infrastructure"

# Lock Hugo version
ENV HUGO_VERSION 0.31.1
ENV HUGO_TAR hugo_${HUGO_VERSION}_Linux-64bit.tar.gz

# Lock Terraform version
ENV TERRAFORM_VERSION 0.11.1
ENV TERRAFORM_ZIP terraform_${TERRAFORM_VERSION}_linux_amd64.zip

# Install package dependencies
RUN apk add --no-cache unzip py-pip ca-certificates

# Install AWS cli tool
RUN pip install awscli

# Download and install Terraform
ADD https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/${TERRAFORM_ZIP} /tmp/terraform.zip
RUN unzip /tmp/terraform.zip -d /usr/local/bin && rm /tmp/terraform.zip

# Download and install Hugo
ADD https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${HUGO_TAR} /tmp/hugo.tar.gz
RUN tar -xzf /tmp/hugo.tar.gz -C /usr/local/bin && rm /tmp/hugo.tar.gz
