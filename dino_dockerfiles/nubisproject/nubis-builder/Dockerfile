# Docker image containing all dependencies for running nubis-builder

# Download and extract dependancies requiring build tools which are not required
#+in the final container
FROM alpine:3.6 AS build-cache
RUN apk add --no-cache \
    bash \
    binutils \
    curl \
    tar \
    unzip
WORKDIR /nubis
# Do not add a 'v' as part of the version string (ie: v1.1.3)
#+ This causes issues with extraction due to GitHub's methodology
#+ Where necesary the 'v' is specified in code below
ENV PackerVersion=1.2.5 \
    TerraformVersion=0.10.7
# Install Packer
RUN ["/bin/bash", "-c", "set -o pipefail \
    && curl --silent -L --out /nubis/packer_${PackerVersion}_linux_amd64.zip https://releases.hashicorp.com/packer/${PackerVersion}/packer_${PackerVersion}_linux_amd64.zip \
    && unzip /nubis/packer_${PackerVersion}_linux_amd64.zip -d /nubis/bin \
    && strip /nubis/bin/packer \
    && rm -f /nubis/packer_${PackerVersion}_linux_amd64.zip" ]
# Install Terraform
RUN ["/bin/bash", "-c", "set -o pipefail \
    && curl --silent -L --out /nubis/terraform_${TerraformVersion}_linux_amd64.zip https://releases.hashicorp.com/terraform/${TerraformVersion}/terraform_${TerraformVersion}_linux_amd64.zip \
    && unzip /nubis/terraform_${TerraformVersion}_linux_amd64.zip -d /nubis/bin \
    && rm -f /nubis/terraform_${TerraformVersion}_linux_amd64.zip" ]


FROM alpine:3.6
ENV PATH=/nubis/nubis-builder/bin:/nubis/bin:$PATH
WORKDIR /nubis
# Install container dependencies
# Cleanup apk cache files
RUN apk add --no-cache \
    bash \
    git \
    jq \
    rsync; \
    rm -f /var/cache/apk/APKINDEX.*
# Copy built dependancies
COPY --from=build-cache /nubis/bin/ /nubis/bin/
# Copy over the bashrc file to dress up the prompt
COPY [ "nubis/docker/bashrc", "/root/.bashrc" ]
# Copy over the nubis-builder-wrapper script
COPY [ "nubis/docker/nubis-builder-wrapper", "/nubis/" ]
# Copy over nubis-builder code
COPY [ "/", "/nubis/nubis-builder/" ]
# Allow everyone to write and copy to that directory
RUN chmod 777 /nubis; \
    chmod 777 /nubis/nubis-builder/secrets
ENTRYPOINT [ "/nubis/nubis-builder-wrapper" ]
CMD [ "help" ]
