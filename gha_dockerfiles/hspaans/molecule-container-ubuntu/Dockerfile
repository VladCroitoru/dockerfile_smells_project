FROM docker.io/ubuntu:22.04

LABEL org.opencontainers.image.description="Ubuntu container for Molecule"
LABEL org.opencontainers.image.source=https://github.com/hspaans/molecule-container-ubuntu

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

# Configure apt and install packages
# hadolint ignore=DL3008
RUN apt-get update \
    && apt-get -y install --no-install-recommends systemd systemd-sysv python3 \
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# Switch back to dialog for any ad-hoc use of apt-get
ENV DEBIAN_FRONTEND=dialog

# Make sure systemd doesn't start agettys on tty[1-6].
RUN rm -f /lib/systemd/system/multi-user.target.wants/getty.target

VOLUME ["/sys/fs/cgroup"]
CMD ["/lib/systemd/systemd"]
