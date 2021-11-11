FROM unitedclassifiedsapps/gitlab-ci-android-fastlane

ENV CLOUD_SDK_VERSION 183.0.0
ENV PATH /google-cloud-sdk/bin:$PATH

RUN apt-get update
RUN apt-get -y install --no-install-recommends \
        fastlane \
        curl \
        python-pip \
        openssh-client \
        git \
    && curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    tar xzf google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    rm google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    ln -s /lib /lib64 && \
    gcloud config set core/disable_usage_reporting true && \
    gcloud config set component_manager/disable_update_check true && \
    gcloud config set metrics/environment github_docker_image && \
    gcloud --version

RUN gcloud init
