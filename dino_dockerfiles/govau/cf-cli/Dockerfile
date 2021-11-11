FROM ubuntu:16.04

ENV CF_CLI_VERSION "6.44.0"
ENV CF_AUTOPILOT_VERSION="0.0.7"

# Install base packages
RUN apt-get update && apt-get -y install \
        curl \
        dnsutils \
        git \
        jq \
        unzip \
        wget && \
    rm -rf /var/lib/apt/lists/*

RUN set -e; \
    curl -L "https://cli.run.pivotal.io/stable?release=linux64-binary&version=${CF_CLI_VERSION}" | tar -zx -C /usr/local/bin; \
    cf install-plugin https://github.com/contraband/autopilot/releases/download/${CF_AUTOPILOT_VERSION}/autopilot-linux -f
