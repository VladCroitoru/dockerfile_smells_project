FROM openjdk:8

MAINTAINER aleksi.hakli@vincit.com

ARG KONTEMPLATE_TAG=v1.3.0
ARG KONTEMPLATE_BIN=kontemplate-1.3.0-98daa6b-linux-amd64.tar.gz
RUN cd /tmp && \
	wget -q https://github.com/tazjin/kontemplate/releases/download/$KONTEMPLATE_TAG/$KONTEMPLATE_BIN && \
	tar xvzf $KONTEMPLATE_BIN && \
	mv kontemplate /usr/local/bin && \
	chown root:root /usr/local/bin/kontemplate && \
	chmod +x /usr/local/bin/kontemplate && \
	rm $KONTEMPLATE_BIN

RUN DEBIAN_FRONTEND=noninteractive apt-get -qy update && \
	apt-get -qy install lsb-release apt-utils git libxml2-utils bash-completion ca-certificates make build-essential
RUN echo "deb http://packages.cloud.google.com/apt cloud-sdk-$(lsb_release -c -s) main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
	curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
RUN DEBIAN_FRONTEND=noninteractive apt-get -qy update && \
	apt-get -qy install kubectl google-cloud-sdk google-cloud-sdk-datastore-emulator google-cloud-sdk-pubsub-emulator google-cloud-sdk-app-engine-go google-cloud-sdk-app-engine-java google-cloud-sdk-app-engine-python google-cloud-sdk-cbt google-cloud-sdk-bigtable-emulator google-cloud-sdk-datalab && apt-get -qy autoremove
