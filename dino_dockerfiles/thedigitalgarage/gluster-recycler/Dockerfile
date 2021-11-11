FROM gluster/gluster-centos:latestclient

RUN INSTALL_PKGS="bash tar jq findutils" && \
    dnf install -y $INSTALL_PKGS && \
    rpm -V $INSTALL_PKGS && \
    dnf clean all

ADD recycler.sh /
CMD /recycler.sh
