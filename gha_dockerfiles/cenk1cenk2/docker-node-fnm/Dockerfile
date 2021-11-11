FROM debian:stable-slim

# Workdir for node package

ENV FNM_VERSION=1.25.0
ENV S6_VERSION 2.2.0.3
ENV FNM_DIR /opt/fnm
ENV FNM_INTERACTIVE_CLI false
ENV FNM_INSTALL_VERSION 16

WORKDIR /tmp

# Install s6 overlay
ADD https://github.com/just-containers/s6-overlay/releases/download/v${S6_VERSION}/s6-overlay-amd64.tar.gz /tmp/
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C / && \
  # create directories
  mkdir -p /etc/services.d && mkdir -p /etc/cont-init.d && mkdir -p /s6-bin

# Install fnm and initiate it
RUN apt-get update && apt-get install -y curl unzip gnupg2 && \
  # install fnm
  curl -fsSL https://fnm.vercel.app/install | bash -s -- --install-dir "/opt/fnm" --skip-shell && \
  ln -s /opt/fnm/fnm /usr/bin/ && chmod +x /usr/bin/fnm && \
  # smoke test for fnm
  /bin/bash -c "fnm -V" && \
  # install latest node version as default
  /bin/bash -c "fnm install ${FNM_INSTALL_VERSION}" && \
  /bin/bash -c "fnm alias default ${FNM_INSTALL_VERSION}" && \
  # add fnm for bash
  printf 'eval "$(fnm env --shell bash)"'>> /root/.bashrc && \
  /bin/bash -c "source /root/.bashrc && fnm use default" && \
  /bin/bash -c "curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -" && \
  /bin/bash -c 'echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list' && \
  /bin/bash -c 'apt-get update && apt-get install -y yarn' && \
  # smoke test
  /bin/bash -c "source /root/.bashrc && node -v" && \
  /bin/bash -c "source /root/.bashrc && npm -v" && \
  /bin/bash -c "source /root/.bashrc && yarn -v" && \
  mkdir -p /data && \
  # clean up build dependencies
  # clean up tmp
  rm -rf /tmp/* && \
  # clean up dependencies
  apt-get remove -y curl unzip gnupg2 && apt-get autoremove -y && \
  # Add running dependencies
  apt-get install -y git

# Copy the supervisor
COPY ./supervisor /cli

# Link and install dependencies
WORKDIR /cli
RUN /bin/bash -c "source /root/.bashrc && yarn --production && yarn link" && \
  # smoke test
  /bin/bash -c "source /root/.bashrc && docker-node-fnm-init -v"

WORKDIR /data

# Create default configuration folders
RUN mkdir -p /scripts

# Copy scripts
ADD https://gist.githubusercontent.com/cenk1cenk2/e03d8610534a9c78f755c1c1ed93a293/raw/2e22e9a5ff34a49f0f5338cd7d137456ba56086f/logger.sh /scripts/logger.sh
RUN chmod +x /scripts/*.sh

# Move s6 supervisor files inside the container
# COPY ./services.d /etc/services.d
COPY ./cont-init.d /etc/cont-init.d

RUN chmod +x /etc/cont-init.d/*.sh

# s6 behaviour, https://github.com/just-containers/s6-overlay
ENV S6_KEEP_ENV 1
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS 2
ENV S6_FIX_ATTRS_HIDDEN 1

ENTRYPOINT ["/bin/bash", "-c", "/init"]
