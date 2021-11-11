FROM garethahealy/centos-pod-pause:1.0

LABEL Name="ocp-external-service-onramp" \
    Vendor="com.garethahealy" \
    Maintainer="garethahealy (https://github.com/garethahealy/)" \
    Version="1.0.1" \
    License="Apache License, Version 2.0"

USER root

ADD run.sh /run.sh
RUN chmod 775 /run.sh

# Install packages without docs. Variable is used to cause yum to fail if missing
RUN INSTALL_PKGS="iptables-services iproute" \
    && yum install -y $INSTALL_PKGS --setopt tsflags=nodocs \
    && rpm -V $INSTALL_PKGS \
    && rm -rf /var/cache/yum \
    && yum -y clean all

ENTRYPOINT ["/run.sh"]



