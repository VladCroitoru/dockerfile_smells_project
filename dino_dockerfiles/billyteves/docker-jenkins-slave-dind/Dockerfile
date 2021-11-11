FROM billyteves/ubuntu-dind

MAINTAINER Billy Ray Teves <billyteves@gmail.com>

ENV SWARM_CLIENT_VERSION 2.2
ENV DOCKER_COMPOSE_VERSION 1.8.0
ENV KUBERNETES_CTL_VERSION v1.4.0

# Add a Jenkins user with permission to run docker commands
RUN useradd -r -m -G docker jenkins

# Install necessary packages
RUN apt-get update && apt-get install -y curl zip openjdk-8-jre-headless supervisor && rm -rf /var/lib/apt/lists/*

# Install Jenkins Swarm Client
RUN wget -q https://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-client/${SWARM_CLIENT_VERSION}/swarm-client-${SWARM_CLIENT_VERSION}-jar-with-dependencies.jar -P /home/jenkins/

# Install Docker Compose
RUN curl -L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose \
    && curl -L https://storage.googleapis.com/kubernetes-release/release/${KUBERNETES_CTL_VERSION}/bin/linux/amd64/kubectl > /usr/local/bin/kubectl \
    && chmod +x /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/kubectl

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["/usr/bin/supervisord"]
