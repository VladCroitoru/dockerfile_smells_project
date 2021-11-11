FROM fedora:latest

RUN dnf install -y cifs-utils && \
    dnf clean all && \
    rm -rf /var/cache/yum

VOLUME ["/target"]

ENTRYPOINT ["cp", "-a", "/sbin/mount.cifs", "/target"]
