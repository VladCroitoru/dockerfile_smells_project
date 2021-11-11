FROM ubuntu:latest

WORKDIR /root
RUN apt-get update -y --fix-missing && \
	apt-get install -y --no-install-recommends && \
	apt-utils && \
	software-properties-common && \
	git-core && \
 	build-essential && \
	libssl-dev libffi-dev && \
	python-dev && \
	wget && \
	curl && \
	unzip && \
	apt-transport-https && \
	jq && \
	nano && \
	vim && \
	apt-add-repository ppa:ansible/ansible -y && \
	apt-get update -y --fix-missing && \
	apt-get install -y ansible && \
	apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ wheezy main" | tee /etc/apt/sources.list.d/azure-cli.list && \
	apt-key adv --keyserver packages.microsoft.com --recv-keys 52E16F86FEE04B979B07E28DB02C46DF417A0893 && \
	apt-get update && \
	apt-get install azure-cli && \
	apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN curl -o terraform.zip https://releases.hashicorp.com/terraform/0.11.2/terraform_0.11.2_linux_amd64.zip && \
	unzip terraform.zip && \
	rm terraform.zip && \
	mv terraform /usr/bin/

RUN curl -o packer.zip https://releases.hashicorp.com/packer/1.1.3/packer_1.1.3_linux_amd64.zip && \
	unzip packer.zip && \
	rm packer.zip && \
	mv packer /usr/bin/

RUN useradd --create-home --shell /bin/bash kenobi
USER kenobi
WORKDIR /home/kenobi
