FROM python:3.9.1-slim

# add docker cli
ARG DOCKER_VERSION="5:19.03.13~3-0~debian-buster"
RUN BUILD_DEPENDENCIES="apt-transport-https curl gnupg-agent software-properties-common" \
	&& apt update \
	&& apt install --yes ca-certificates ${BUILD_DEPENDENCIES} \
	&& curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add \
	&& add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" \
	&& apt update \
	&& apt -y install docker-ce-cli=${DOCKER_VERSION} \
	&& apt -y purge ${BUILD_DEPENDENCIES} \
	&& apt autoremove --yes \
	&& rm -rf /var/lib/apt/lists/*

# install dependencies for kirin fabric
COPY requirements.txt /
RUN pip install -r /requirements.txt -U

# setup kirin fabric
RUN mkdir /fabfile
COPY fabfile /fabfile
WORKDIR /fabfile
ENV PYTHONPYCACHEPREFIX=/tmp
