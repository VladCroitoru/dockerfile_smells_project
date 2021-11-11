FROM centos:7

# Copy extra files to the image.
COPY ./root/ /

# When bash is started non-interactively, to run a shell script, for example it
# looks for this variable and source the content of this file. This will enable
# the SCL for all scripts without need to do 'scl enable'.
ENV BASH_ENV=/etc/scl_enable \
    ENV=/etc/scl_enable \
    PROMPT_COMMAND=". /etc/scl_enable"

RUN yum install -y centos-release-scl-rh && \
    BUILD_PKGS="autoconf \
        automake \
        bzip2 \
        gcc-c++ \
        gd-devel \
        libcurl-devel \
        libxml2-devel \
        libxslt-devel \
        make \
        mariadb-devel \
        mariadb-libs \
        openssl-devel \
        patch \
        postgresql-devel \
        procps-ng \
        sqlite-devel \
        unzip \
        wget \
        zlib-devel" && \
    INSTALL_PKGS="rh-ruby24 \
        rh-ruby24-ruby-devel \
        rh-ruby24-rubygem-rake \
        rh-ruby24-rubygem-bundler" && \
    yum install -y --setopt=tsflags=nodocs $BUILD_PKGS $INSTALL_PKGS && rpm -V $BUILD_PKGS $INSTALL_PKGS && \
    yum clean all -y

ENTRYPOINT ["/usr/bin/container-entrypoint"]

