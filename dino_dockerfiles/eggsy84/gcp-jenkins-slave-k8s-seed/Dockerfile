FROM jenkinsci/jnlp-slave
MAINTAINER James Heggs jimbobegg@hotmail.com

ENV CLOUDSDK_CORE_DISABLE_PROMPTS 1
ENV PATH /opt/google-cloud-sdk/bin:$PATH

USER root

# Install Google Cloud Components
RUN curl https://sdk.cloud.google.com | bash && mv google-cloud-sdk /opt
RUN gcloud components install kubectl

# Install docker
RUN curl -fsSL https://get.docker.com/ | sh

# Required for ensuring we use the Gcloud docker API version
ENV DOCKER_API_VERSION=1.21

# Install maven
RUN mkdir -p "/opt" && \
    cd /tmp && \
    wget "http://archive.apache.org/dist/maven/maven-3/3.2.5/binaries/apache-maven-3.2.5-bin.tar.gz" && \
    tar -zxvf "apache-maven-3.2.5-bin.tar.gz" && \
    mv "apache-maven-3.2.5" "/opt" && \
    ln -s "/opt/apache-maven-3.2.5/bin/mvn" /usr/bin/mvn
