FROM jenkins/jenkins:lts

USER root

RUN apt-get update; \
  # Connect git-lfs repo
  curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash; \
  # Install various packages
  apt-get install -y apt-transport-https dirmngr sudo rsync git-lfs file \
  && apt-get autoclean \
  && apt-get autoremove

# Install Docker
RUN curl https://get.docker.com/ | bash

# Install all versions of Docker Compose from 1.20 on
SHELL ["/bin/bash", "-c"]
RUN TAGS=$(git ls-remote https://github.com/docker/compose | grep refs/tags | grep -oP '[0-9]+\.[2-9][0-9]+\.[0-9]+$'); \
  for COMPOSE_VERSION in $TAGS; do \
  export FILE="/usr/local/bin/docker-compose-${COMPOSE_VERSION}" && \
  echo "Fetching Docker Compose version ${COMPOSE_VERSION} to ${FILE}" && \
  curl -L "https://github.com/docker/compose/releases/download/${COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o "${FILE}" && \
  # Occasionally the tag will be created but there won't be a release yet so check we have an executable.
  if [[ "$(file --brief --mime-type ${FILE})" == "application/x-executable" ]]; then LATEST="${FILE}"; else rm "${FILE}"; fi; \
  done; \
  chmod a+x /usr/local/bin/docker-compose-* && \
  echo "Symlinking most recent stable Docker Compose version: ${LATEST}" && \
  ln -s "${LATEST}" /usr/local/bin/docker-compose

# Configure jenkins user
RUN usermod -aG docker jenkins && usermod -aG sudo jenkins && id jenkins
RUN echo "jenkins ALL=(ALL)	NOPASSWD: ALL" >> /etc/sudoers

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]

USER jenkins
RUN git lfs install

EXPOSE 8080
