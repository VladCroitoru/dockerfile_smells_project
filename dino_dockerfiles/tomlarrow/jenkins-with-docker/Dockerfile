FROM jenkins
USER root

RUN apt-get update && \
    apt-get install -y sudo apt-transport-https ca-certificates curl software-properties-common && \
    rm -rf /var/lib/apt/lists/* && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" && \
    apt-get update && \
    apt-cache policy docker-ce && \
    apt-get install -y docker-ce && \
    echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers

USER jenkins
