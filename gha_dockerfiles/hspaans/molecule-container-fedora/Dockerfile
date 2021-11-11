FROM docker.io/fedora:35

LABEL org.opencontainers.image.description="Fedora container for Molecule"
LABEL org.opencontainers.image.source=https://github.com/hspaans/molecule-container-fedora

# Configure apt and install packages
# hadolint ignore=DL3033
RUN yum -y install systemd systemd-sysv python3 \
    # Clean up
    && yum clean all

# Make sure systemd doesn't start agettys on tty[1-6].
RUN rm -f /lib/systemd/system/multi-user.target.wants/getty.target

VOLUME ["/sys/fs/cgroup"]
CMD ["/lib/systemd/systemd"]
