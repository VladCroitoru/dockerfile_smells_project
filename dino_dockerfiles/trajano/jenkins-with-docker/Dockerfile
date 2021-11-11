FROM jenkins/jenkins:latest
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common \
    apt-transport-https \
    ca-certificates \
 && curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - \
 && add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/debian stretch stable"
RUN apt-get update && apt-get install -y docker-ce
USER jenkins
COPY docker-slaves.xml /usr/share/jenkins/ref/
RUN /usr/local/bin/install-plugins.sh \
  docker-slaves \
  github-branch-source \
  github-organization-folder \
  pipeline-github-lib \
  antisamy-markup-formatter \
  workflow-aggregator \
  ws-cleanup
