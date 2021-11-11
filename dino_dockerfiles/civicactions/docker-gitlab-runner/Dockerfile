FROM gitlab/gitlab-runner:v12.7.1

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install Docker
RUN curl -sSL https://get.docker.com/ | sh

# Install all versions of Docker Compose from 1.20 on
RUN TAGS=$(git ls-remote https://github.com/docker/compose | grep refs/tags | grep -oP '[0-9]+\.[2-9][0-9]+\.[0-9]+$'); \
  for COMPOSE_VERSION in $TAGS; do \
  export FILE="/usr/local/bin/docker-compose-${COMPOSE_VERSION}" && \
  echo "Fetching Docker Compose version ${COMPOSE_VERSION} to ${FILE}" && \
  curl -L "https://github.com/docker/compose/releases/download/${COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o "${FILE}" && \
  # Occasionally the tag will be created but there won't be a release yet so check we have an executable.
  if [[ "$(/usr/bin/file --brief --mime-type ${FILE})" == "application/x-executable" ]]; then LATEST="${FILE}"; else rm "${FILE}"; fi; \
  done; \
  chmod a+x /usr/local/bin/docker-compose-* && \
  echo "Symlinking most recent stable Docker Compose version: ${LATEST}" && \
  ln -s "${LATEST}" /usr/local/bin/docker-compose

# Install git lfs and rsync
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash && \
  apt-get -y install git-lfs rsync
