FROM centos:7

ENV NFSTRACE_VERSION 0.4.3.2

RUN yum -y install centos-release-scl epel-release \
        && yum -y install \
            cmake3 \
            devtoolset-4-binutils \
            devtoolset-4-gcc* \
            libpcap-devel \
            make \
        && yum -y clean all

RUN mkdir -p /build \
        && cd /build \
        && curl -fsSL -o nfstrace-${NFSTRACE_VERSION}.tar.gz "https://github.com/epam/nfstrace/archive/${NFSTRACE_VERSION}.tar.gz" \
        && tar xzf nfstrace-${NFSTRACE_VERSION}.tar.gz \
        && rm nfstrace-${NFSTRACE_VERSION}.tar.gz \
        && cd nfstrace-${NFSTRACE_VERSION} \
        && mkdir release \
        && cd release \
        && scl enable devtoolset-4 "cmake3 -DCMAKE_BUILD_TYPE=release ../" \
        && make -j4 \
        && make install \
        && cd / \
        && rm -rf /build
