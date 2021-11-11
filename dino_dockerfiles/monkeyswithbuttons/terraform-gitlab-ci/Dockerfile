FROM alpine:latest
MAINTAINER Greg Trahair <greg@monkeyswithbuttons.com>

# Set the version you want
ENV TERRAFORM_VERSION=0.10.6

# Disable Checkpoint
ENV CHECKPOINT_DISABLE=1

# Install packages we need
RUN apk add --no-cache --update git wget make openssh-client

# Get the terraform package and checksum file
ADD https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip ./
ADD https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_SHA256SUMS ./

# Remove all but the linux_amd64 sha256sum from the checksum file
RUN sed -i "/terraform_${TERRAFORM_VERSION}_linux_amd64.zip/!d" terraform_${TERRAFORM_VERSION}_SHA256SUMS

# Verify the checksum
RUN sha256sum -cs terraform_${TERRAFORM_VERSION}_SHA256SUMS

# Extract the binary and remove the archive
RUN unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /bin
RUN rm -f terraform_${TERRAFORM_VERSION}_linux_amd64.zip
