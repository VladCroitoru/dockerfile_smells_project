FROM fedora:latest
MAINTAINER Michael Altizer <mialtize@cisco.com>

# Add /usr/local/lib and /usr/local/lib64 to the ldconfig caching paths
ADD ldconfig-local.conf /etc/ld.so.conf.d/local.conf

RUN \
# Update the image's pre-installed packages
dnf upgrade --refresh -y && \
# Install the Snort build dependencies
dnf install -y \
    autoconf \
    automake \
    cmake \
    file \
    flatbuffers-devel \
    gcc-c++ \
    gperftools-devel \
    hwloc-devel \
    hyperscan-devel \
    libdnet-devel \
    libmnl-devel \
    libpcap-devel \
    libtool \
    libunwind-devel \
    libuuid-devel \
    luajit-devel \
    make \
    openssl-devel \
    pcre-devel \
    xz-devel \
    zlib-devel \
&& \
# Install the Snort developer conveniences
dnf install -y \
    gdb \
    git \
    libasan \
    libtsan \
    vim \
&& \
# Install programs necessary for documentation generation
# dnf install asciidoc dblatex w3m && \
# Clean out the DNF cache
dnf clean all
