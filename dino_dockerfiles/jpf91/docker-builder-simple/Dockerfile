FROM buildpack-deps:jessie

# Set root password to root. Useful when debugging this container to install new packages
RUN echo "root:root" | chpasswd

# A workaround for GCC checking for /usr/lib32 on the local system
RUN mkdir -p /usr/lib32 \
    && mkdir -p /usr/lib64

# Install build requirements
# libc6-i386: Some x86 compiler builds try to run 32bit executables locally
# for link tests. This is annoying, but not a real problem.
RUN apt-get update && apt-get install -y \
        bison \
        flex \
        gawk \
        texinfo \
        libtool \
        automake \
        xz-utils \
        p7zip \
        bash \
        gzip \
        autoconf \
        m4 \
        libc6-i386 \
        nfs-common \
    && apt-get remove -y gcc gcc-4.9 g++ g++-4.9 libstdc++-4.9-dev binutils  cpp cpp-4.9 libasan1 libatomic1 libcilkrts5 libcloog-isl4 libgcc-4.9-dev libisl10 libitm1 liblsan0 libmpc3 libquadmath0 libtsan0 libubsan0 liblsan0 libmpc3 libquadmath0 libtsan0 libubsan0 \
    && apt-get install -y libatomic1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN echo "nfs-cache.lan:/ /home/build/nfs nfs4 rw,noauto,user,exec,nosuid,nodev 0 0" >> /etc/fstab

# Add build user
RUN adduser --disabled-password --gecos "" build \
    && echo "build:build" | chpasswd \
    && chsh -s /bin/bash build \
    && echo "dash dash/sh boolean false" | debconf-set-selections \
    && DEBIAN_FRONTEND=noninteractive dpkg-reconfigure dash

# install dub
RUN mkdir build && cd build \
    && wget --no-verbose http://code.dlang.org/files/dub-1.0.0-linux-x86_64.tar.gz \
    && tar xf dub-1.0.0-linux-x86_64.tar.gz \
    && cp dub /usr/bin/ \
    && cd ../../ && rm -rf build

# Install host toolchains
ADD create_links.sh /usr/local/bin/
ADD setup_host_toolchains.sh /usr/local/bin/
ADD gdc_build_tools.tar.gz /usr/local/bin/

# Initialize /home/build directory
WORKDIR /home/build
USER build

RUN /usr/local/bin/setup_host_toolchains.sh
RUN mkdir /home/build/nfs
ADD gccbuild.json /home/build/.config/gccbuild.json
