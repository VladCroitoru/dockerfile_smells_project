FROM boot2docker/boot2docker
RUN curl -L -o $ROOTFS/usr/local/bin/docker https://experimental.docker.com/builds/Linux/x86_64/docker-latest && \
    chmod +x $ROOTFS/usr/local/bin/docker && \
    { $ROOTFS/usr/local/bin/docker version || true; }
RUN /make_iso.sh
RUN sha256sum boot2docker.iso
