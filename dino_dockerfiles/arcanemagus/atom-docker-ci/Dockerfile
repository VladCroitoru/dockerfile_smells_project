FROM ubuntu:latest

LABEL maintainer="Landon Abney <landonabney@gmail.com>"
LABEL description="An image to run Atom packages in for CI builds."

ENV LANG="C.UTF-8" DISPLAY=":99"

# Add the atom user as a sudo-enabled account
RUN useradd --create-home --home-dir "/home/atom" --user-group --groups sudo atom

# Enable passwordless sudo for users under the "sudo" group
RUN mkdir --parents /etc/sudoers.d
RUN echo "%sudo ALL=NOPASSWD:ALL" > /etc/sudoers.d/sudo-no-passwd
RUN chmod 0440 /etc/sudoers.d/sudo-no-passwd
WORKDIR "/home/atom"

# Add Xvfb and have it start at boot
COPY xvfb_start.sh /usr/local/bin/xvfb_start
RUN chmod 0655 /usr/local/bin/xvfb_start
ENTRYPOINT ["/usr/local/bin/xvfb_start"]

# Set the Atom version and paths to executables
ENV ATOM_VERSION=v1.47.0-beta0 ATOM_SCRIPT_PATH=atom-beta APM_SCRIPT_PATH=apm-beta

# Install dependencies
RUN apt-get update && \
    apt-get install --assume-yes --quiet \
                    --no-install-suggests --no-install-recommends \
      git \
      ssh \
      tar \
      gzip \
      ca-certificates \
      \
      build-essential \
      fakeroot \
      libsecret-1-dev \
      \
      xvfb \
      libxss1 \
      libasound2 \
      libgtk-3-0 \
      \
      sudo \
      curl \
      && \
    \
    curl --silent --location \
      "https://github.com/atom/atom/releases/download/${ATOM_VERSION}/atom-amd64.deb" \
      --header 'Accept: application/octet-stream' \
      --output "/tmp/atom-amd64.deb" && \
    dpkg --unpack "/tmp/atom-amd64.deb" && \
    apt-get install --fix-broken \
      --assume-yes --quiet --no-install-suggests --no-install-recommends && \
    \
    apt-get clean && \
    rm --force /tmp/atom-amd64.deb && \
    rm --recursive --force /var/lib/apt/lists/*

USER atom:atom
