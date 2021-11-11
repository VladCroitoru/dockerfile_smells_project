### LOCAL BUILD COMMAND
# docker build -t self-managed-osdu --build-arg WORKING_DIRECTORY=/osdu-azure/templates/osdu-r3-mvp/central_resources .
# --build-arg SSH_PRIVATE_KEY="$(cat ~/.ssh/id_rsa)" --build-arg SSH_PUBLIC_KEY="$(cat ~/.ssh/id_rsa.pub)" .
# docker run -it --env-file .env -it self-managed-osdu --env TF_VAR_workspace="cr-local" --workdir /osdu-azure/templates/osdu-r3-mvp/central_resources

# You can pick any Debian/Ubuntu-based image. 😊
# FROM mcr.microsoft.com/vscode/devcontainers/base:buster
FROM debian:buster

COPY scripts/*.sh /tmp/library-scripts/

# [Option] Install zsh
ARG INSTALL_ZSH="true"

# [Option] Upgrade OS packages to their latest versions
ARG UPGRADE_PACKAGES="false"

# Install needed packages and setup non-root user. Use a separate RUN statement to add your own dependencies.
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
  && bash /tmp/library-scripts/common-debian.sh "${INSTALL_ZSH}" "${USERNAME}" "${USER_UID}" "${USER_GID}" "${UPGRADE_PACKAGES}" "true" "true" \
  && apt-get install -y graphviz \
  && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# [Option] Install Azure CLI
ARG INSTALL_AZURE_CLI="true"

# [Option] Install Docker CLI
ARG INSTALL_DOCKER="false"

# [Option] Install Node.js
ARG INSTALL_NODE="false"
ARG NODE_VERSION="lts/*"
ENV NVM_DIR=/usr/local/share/nvm
ENV NVM_SYMLINK_CURRENT=true \
  PATH=${NVM_DIR}/current/bin:${PATH}
RUN if [ "${INSTALL_AZURE_CLI}" = "true" ]; then bash /tmp/library-scripts/azcli-debian.sh; fi \
  && if [ "${INSTALL_NODE}" = "true" ]; then bash /tmp/library-scripts/node-debian.sh "${NVM_DIR}" "${NODE_VERSION}" "${USERNAME}"; fi \
  && if [ "${INSTALL_DOCKER}" = "true" ]; then \
  bash /tmp/library-scripts/docker-debian.sh "true" "/var/run/docker-host.sock" "/var/run/docker.sock" "${USERNAME}"; \
  else \
  echo '#!/bin/bash\n"$@"' > /usr/local/share/docker-init.sh && chmod +x /usr/local/share/docker-init.sh; \
  fi \
  && rm -rf /var/lib/apt/lists/*


# Install Infra Azure Provisioning
ARG OSDU_VERSION=v0.11.0
RUN bash /tmp/library-scripts/osdu-infra.sh

# Install Terraform, tflint, Terragrunt
ARG TERRAFORM_VERSION=0.14.10
ARG TFLINT_VERSION=0.8.2
ARG TERRAGRUNT_VERSION=0.28.1
RUN bash /tmp/library-scripts/terraform-debian.sh "${TERRAFORM_VERSION}" "${TFLINT_VERSION}" "${TERRAGRUNT_VERSION}"

# Copy Customizations
COPY customizations/modules/providers/azure /osdu-azure/modules/providers/azure
COPY customizations/templates /osdu-azure/templates/osdu-r3-mvp

# Copy Configurations
COPY configuration/controlplane.tfvars /osdu-azure/templates/osdu-r3-mvp/central_resources/custom.tfvars
COPY configuration/dataplane.tfvars /osdu-azure/templates/osdu-r3-mvp/service_resources/custom.tfvars
COPY configuration/partition.tfvars /osdu-azure/templates/osdu-r3-mvp/data_partition/custom.tfvars

# Create SSH Keys
ARG SSH_PUBLIC_KEY
RUN mkdir -p /osdu-azure/.ssh && chmod 0700 /osdu-azure/.ssh
RUN touch /osdu-azure/.ssh/id_rsa && chmod 600 /osdu-azure/.ssh/id_rsa
RUN echo "$SSH_PUBLIC_KEY" > /osdu-azure/.ssh/id_rsa.pub && chmod 600 /osdu-azure/.ssh/id_rsa.pub


# Change Template Working Directory
ARG WORKING_DIRECTORY
WORKDIR ${WORKING_DIRECTORY}

ENTRYPOINT [ "/usr/local/bin/deploy" ]
CMD [ "run" ]
