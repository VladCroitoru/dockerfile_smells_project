FROM python:3.9.7-alpine3.13

LABEL org.opencontainers.image.source = "https://github.com/neuro-inc/neuro-extras"

ENV LANG C.UTF-8
ENV PYTHONUNBUFFERED 1

ARG CLOUD_SDK_VERSION=347.0.0
ENV CLOUD_SDK_VERSION=$CLOUD_SDK_VERSION

ENV PATH /google-cloud-sdk/bin:$PATH

# TODO (semendiak): 'gcc g++ libffi-dev' are needed for upstream dependency cffi
# some of the latest releases (not in our repo) broke installation without those libs as for 27.09.2021
RUN apk add --no-cache make curl git rsync unrar zip unzip vim wget openssh-client ca-certificates bash gcc g++ libffi-dev

# Install Google Cloud SDK
RUN wget -q https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    tar xzf google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    rm google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz && \
    ln -s /lib /lib64 && \
    gcloud config set core/disable_usage_reporting true && \
    gcloud --version

# Install rclone
RUN curl -O https://downloads.rclone.org/rclone-current-linux-amd64.zip && \
    unzip rclone-current-linux-amd64.zip && \
    rm rclone-current-linux-amd64.zip && \
    cp rclone-*-linux-amd64/rclone /usr/bin/ && \
    rm -rf rclone-*-linux-amd64 && \
    chmod 755 /usr/bin/rclone

# Install kubectl
RUN cd /usr/local/bin && \
    wget https://storage.googleapis.com/kubernetes-release/release/v1.8.0/bin/linux/amd64/kubectl && \
    chmod +x ./kubectl && \
    kubectl version --client

# package version is to be overloaded with exact version
ARG NEURO_EXTRAS_PACKAGE=neuro-extras

ENV PATH=/root/.local/bin:$PATH

RUN pip3 install --no-cache-dir -U pip pipx
RUN MULTIDICT_NO_EXTENSIONS=1 YARL_NO_EXTENSIONS=1 pip install --user \
    $NEURO_EXTRAS_PACKAGE \
    # used in outforz, not in reqs file since NF itself requires NE
    neuro-flow==21.7.9 && \
    pipx install awscli # isolated env since it has conflicts with neuro-cli
RUN neuro-extras init-aliases

RUN mkdir -p /root/.ssh
COPY files/ssh/known_hosts /root/.ssh/known_hosts

VOLUME ["/root/.config"]

WORKDIR /root

COPY docker.entrypoint.sh /var/lib/neuro/entrypoint.sh
ENTRYPOINT ["/var/lib/neuro/entrypoint.sh"]
