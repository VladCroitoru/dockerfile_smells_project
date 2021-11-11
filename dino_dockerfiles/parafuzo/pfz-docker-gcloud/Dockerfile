FROM docker:git

RUN apk update && apk add wget bash python docker && rm -rf /var/cache/apk/*

# Install the Google Cloud SDK.
ENV HOME /
ENV CLOUDSDK_PYTHON_SITEPACKAGES 1
RUN wget https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip && unzip google-cloud-sdk.zip && rm google-cloud-sdk.zip
RUN google-cloud-sdk/install.sh --usage-reporting=true --path-update=true --bash-completion=true --rc-path=/.bashrc --additional-components app-engine-java app-engine-python app kubectl alpha beta gcd-emulator pubsub-emulator

# Disable updater check for the whole installation.
RUN google-cloud-sdk/bin/gcloud config set --installation component_manager/disable_update_check true

# Disable updater completely.
RUN sed -i -- 's/\"disable_updater\": false/\"disable_updater\": true/g' /google-cloud-sdk/lib/googlecloudsdk/core/config.json

RUN mkdir /.ssh
ENV PATH /google-cloud-sdk/bin:$PATH

COPY gcloud-auth.sh /app/
WORKDIR /app

CMD ["/bin/bash"]
