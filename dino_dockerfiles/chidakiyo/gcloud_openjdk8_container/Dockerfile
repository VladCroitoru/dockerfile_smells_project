FROM gcr.io/google_appengine/openjdk:8

# Install modules
RUN apt-get update && apt-get install -y --no-install-recommends \
	g++ \
	gcc \
	vim \
	libc6-dev \
	make \
	git \
	python \
	wget \
	&& rm -rf /var/lib/apt/lists/* && apt-get clean

# Install golang
ENV GOPATH=/usr/local/lib/go
ENV GOROOT=/usr/local/go
ENV PATH=$PATH:$GOROOT/bin:$GOPATH/bin

RUN wget https://dl.google.com/go/go1.11.linux-amd64.tar.gz -O golang.tar.gz && tar -zxvf golang.tar.gz && mv go ${GOROOT}

# Install the Google Cloud SDK.
ENV HOME /
ENV CLOUDSDK_PYTHON_SITEPACKAGES 1
RUN wget https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip && unzip google-cloud-sdk.zip && rm google-cloud-sdk.zip
RUN google-cloud-sdk/install.sh --usage-reporting=true --path-update=true --bash-completion=true --rc-path=/.bashrc --additional-components app-engine-java app-engine-python app kubectl alpha beta gcd-emulator pubsub-emulator cloud-datastore-emulator app-engine-go bigtable

# Disable updater check for the whole installation.
# Users won't be bugged with notifications to update to the latest version of gcloud.
RUN google-cloud-sdk/bin/gcloud config set --installation component_manager/disable_update_check true

# Disable updater completely.
# Running `gcloud components update` doesn't really do anything in a union FS.
# Changes are lost on a subsequent run.
RUN sed -i -- 's/\"disable_updater\": false/\"disable_updater\": true/g' /google-cloud-sdk/lib/googlecloudsdk/core/config.json

RUN mkdir /.ssh
ENV PATH /google-cloud-sdk/bin:$PATH
VOLUME ["/.config"]
CMD ["/bin/bash"]
