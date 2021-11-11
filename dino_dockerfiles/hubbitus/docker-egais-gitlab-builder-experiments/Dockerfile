# https://hub.docker.com/_/fedora

# Amazon ECR credential-helper
# @see https://github.com/awslabs/amazon-ecr-credential-helper
FROM golang:1.14.2-buster AS dependencies

RUN go get -u github.com/awslabs/amazon-ecr-credential-helper/ecr-login/cli/docker-credential-ecr-login

#------------------------------------------
FROM fedora:31

LABEL MAINTAINER="Pavel Alexeev <Pahan@Hubbitus.info>"

COPY --from=dependencies /go/bin/docker-credential-ecr-login /usr/bin/

RUN dnf install -y 'dnf-command(config-manager)' \
	&& dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo \
	&& dnf copr enable cerenit/helm -y \
		&& dnf clean all

# We don't fair it will be fat - it intended to start faster many times. So, single download time have no many sence.
RUN dnf install -y \
		docker-ce-cli containerd.io docker-compose \
		kubernetes-client helm \
		java-1.8.0-openjdk-devel java-1.8.0-openjdk-headless \
		jq \
		ruby \
		git \
		gzip which `# For sencha installer` \
		httpie \
		chromium \
	&& dnf clean all
