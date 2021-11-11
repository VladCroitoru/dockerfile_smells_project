FROM ubuntu:16.04

LABEL maintainer "r.bolte@gmail.com"

## Install prerequisites, Docker (client-only), Google Cloud SDK and Kubernetes (kubectl)
## Most commands are shamelessly stolen from CircleCI (https://circleci.com/docs/2.0/building-docker-images/) and Google Cloud docker container (https://github.com/GoogleCloudPlatform/cloud-sdk-docker/blob/master/Dockerfile)

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y; \
	apt-get install -y \
	apt-utils \
	python \
	unzip \
	curl; \
	curl -fsSL get.docker.com | /bin/sh; \
	curl -fsSLO https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip; \
	unzip google-cloud-sdk.zip; \
	rm google-cloud-sdk.zip; \
	google-cloud-sdk/install.sh --usage-reporting=true --path-update=true --bash-completion=true --rc-path=/.bashrc --additional-components kubectl alpha beta; \
	google-cloud-sdk/bin/gcloud config set --installation component_manager/disable_update_check true; \
	export PATH=/google-cloud-sdk/bin:$PATH; \
	docker --version; \
	gcloud --version; \
	kubectl version --client;

ENV PATH=/google-cloud-sdk/bin:$PATH

CMD ["/bin/bash"]