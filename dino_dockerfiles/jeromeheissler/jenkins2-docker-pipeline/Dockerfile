FROM jenkins/jenkins:latest

# Install sudo and make jenkins sudoer to be able to call docker with sudo from inside jenkins container
USER root

RUN apt-get update && apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg2 \
    jq \
    libfontconfig \
    software-properties-common \
    sudo

RUN curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | apt-key add - && \
    add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
    $(lsb_release -cs) \
    stable"

RUN apt-get update && apt-get install -y docker-ce && rm -rf /var/lib/apt/lists/*

RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers
RUN usermod -aG docker jenkins

USER jenkins
