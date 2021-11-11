# Docker image containing all dependencies for releasing Nubis

# Downloading release of hub from github does not work on alpine linux see:
# https://github.com/github/hub/issues/1645
# As a result, build it on alpine and copy it into the release container
FROM alpine:3.6 AS build-hub
RUN apk add --no-cache \
    bash \
    go=1.8.4-r0 \
    libc-dev=0.7.1-r0 \
    git=2.13.7-r0
WORKDIR /app
RUN ["/bin/bash", "-c", "set -o pipefail \
    && git clone https://github.com/github/hub.git \
    && cd hub \
    && git fetch --tags \
    && git checkout v2.2.9 \
    && ./script/build " ]


FROM alpine:3.6
WORKDIR /nubis

# Install container dependencies
RUN apk add --no-cache \
    bash \
    curl \
    docker \
    file \
    git \
    jq \
    nodejs \
    nodejs-npm \
    openssl \
    py-pip \
    ruby \
    ruby-irb \
    ruby-rdoc \
    zip; \
    rm -f /var/cache/apk/APKINDEX.*

# Do not add a 'v' as pert of the version string (ie: v1.1.3)
#+ This causes issues with extraction due to GitHub's methodology
#+ Where necessary the 'v' is specified in code below
# Set up the path to include our code and utilities
ENV GhiVersion=1.2.0 \
    ChangelogGeneratorVersion=1.14.1 \
    PATH=/nubis/bin:$PATH

# Install gem dependencies
# Set up the directory structure for the code and utilities
# Create empty gitconfig, git-credentials and hub files
#+ This is for runtime mounting of file volumes
RUN gem install ghi -v ${GhiVersion}; \
    gem install rake; \
    gem install github_changelog_generator -v ${ChangelogGeneratorVersion}; \
    pip install awscli; \
    mkdir -p /nubis/.repositories /root/.config; \
    touch /root/.gitconfig /root/.git-credentials-seed /root/.config/hub

# Install hub
COPY --from=build-hub /app/hub/bin/hub /nubis/bin/hub

# Copy over the bashrc file to dress up the prompt
COPY [ "nubis/docker/bashrc", "/root/.bashrc" ]

# Copy over nubis-release code
COPY [ "bin/", "/nubis/bin/" ]

# Copy over the nubis-release-wrapper script
COPY [ "nubis/docker/nubis-release-wrapper", "/nubis/nubis-release/" ]

# Set the entry-point to the wrapper script
ENTRYPOINT [ "/nubis/nubis-release/nubis-release-wrapper" ]

# Give the people some useful information
CMD [ "help" ]
#CMD [ "/bin/bash" ]
