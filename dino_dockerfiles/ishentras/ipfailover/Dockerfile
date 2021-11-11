#
# VIP failover monitoring container for OpenShift Origin.
#
#
FROM fedora

RUN INSTALL_PKGS="kmod keepalived iproute psmisc nmap-ncat net-tools" && \
    dnf install -y $INSTALL_PKGS && \
    rpm -V $INSTALL_PKGS && \
    dnf clean all
COPY . /var/lib/ipfailover/keepalived/

LABEL io.k8s.display-name="OpenShift Origin IP Failover" \
      io.k8s.description="This is a component of OpenShift Origin and runs a clustered keepalived instance across multiple hosts to allow highly available IP addresses."
EXPOSE 1985
WORKDIR /var/lib/ipfailover
ENTRYPOINT ["/var/lib/ipfailover/keepalived/monitor.sh"]
