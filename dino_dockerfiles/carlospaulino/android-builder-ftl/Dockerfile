FROM carlospaulino/android-builder:1.0.3

LABEL version="1.0.3" \
  maintainer="Carlos Paulino" \
  maintainer.email="cpaulino@gmail.com" \
  description="Android Build Docker image with support for Firebase Test Lab" \
  repository="https://github.com/carlospaulino/android-builder-ftl"

# setup gcloud
RUN apt-get install curl apt-transport-https -y \
  && echo "deb https://packages.cloud.google.com/apt cloud-sdk-xenial main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
  && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - \
  && apt-get update \
  && apt-get install google-cloud-sdk -y \
  && apt-get clean

WORKDIR /tmp/project
