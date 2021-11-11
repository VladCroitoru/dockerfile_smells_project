FROM registry.fedoraproject.org/fedora:29
LABEL maintainer="Micah Abbott <miabbott@redhat.com>"
RUN dnf -y install ostree python2 rsync && \
    dnf clean all && \
    curl -L -o /root/rsync-repos https://raw.githubusercontent.com/ostreedev/ostree-releng-scripts/master/rsync-repos && \
    chmod +x /root/rsync-repos
COPY mirror.sh /root/
ENTRYPOINT ["/root/mirror.sh"]
