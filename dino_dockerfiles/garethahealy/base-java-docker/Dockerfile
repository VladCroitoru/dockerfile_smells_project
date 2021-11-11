FROM fabric8/java-centos-openjdk8-jdk:1.4.0

LABEL Name="base-java-docker" \
    Vendor="com.garethahealy" \
    Maintainer="garethahealy (https://github.com/garethahealy/)" \
    Version="1.4.0-2" \
    License="Apache License, Version 2.0"

# Install packages without docs. Variable is used to cause yum to fail if missing
RUN INSTALL_PKGS="curl" \
    && yum install -y $INSTALL_PKGS --setopt tsflags=nodocs \
    && rpm -V $INSTALL_PKGS \
    && rm -rf /var/cache/yum \
    && yum -y clean all
