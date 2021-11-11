FROM docker:stable as dockerclient

FROM maven:latest
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
        bash \
        git \
        procps \
        openssh-client \
        curl \
        less \
        groff \
        jq \
        python3 \
        python3-pip && \
    pip3 install --upgrade pip awscli && \
    mkdir /root/.aws
COPY --from=dockerclient /usr/local/bin/docker /usr/local/bin/docker
