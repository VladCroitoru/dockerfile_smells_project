FROM fedora:33
MAINTAINER Rob Thijssen <rthijssen@gmail.com>

RUN curl https://packages.microsoft.com/keys/microsoft.asc > ./microsoft.asc
RUN rpm --import ./microsoft.asc
RUN rpm -Uvh https://packages.microsoft.com/config/rhel/7/packages-microsoft-prod.rpm
RUN dnf update -y && dnf clean all
RUN dnf install -y \
    cmake \
    gcc \
    git \
    gnupg2 \
    jq \
    nodejs \
    npm \
    openssl-devel \
    powershell \
    pwgen \
    python \
    python-pip \
    ruby-devel \
    unzip \
    uuid \
    && dnf clean all
RUN pip install --upgrade pip
RUN pip install \
    awscli \
    boto3 \
    requests \
    yq
RUN npm install jsonlint -g
RUN gem install papertrail
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
