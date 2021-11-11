FROM registry.fedoraproject.org/fedora
RUN dnf -y install qemu-user-static && dnf clean all
COPY LICENSE entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
ARG IMAGE=ghcr.io/nalind/fedora-qemu-user-static
ENV IMAGE=${IMAGE}
ARG SOURCE=https://github.com/nalind/fedora-qemu-user-static
LABEL org.opencontainers.image.source=${SOURCE}
