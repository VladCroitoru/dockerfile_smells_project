FROM fedora:latest

RUN yum -y update && yum -y install git make gcc p7zip p7zip-plugins bzip2

# CoreOS Linux Kernel
ENV KERNEL_VERSION 3.17.2
RUN cd /usr/src && \
    git clone --depth 1 --single-branch -b coreos/v${KERNEL_VERSION} https://github.com/coreos/linux.git
RUN cd /usr/src/linux && \
    curl -L -o .config https://raw.githubusercontent.com/coreos/coreos-overlay/master/sys-kernel/coreos-kernel/files/x86_64_defconfig-${KERNEL_VERSION} && \
    make prepare && make scripts

# VirtualBox Guest Additions
ENV VBOX_VERSION 4.3.18
RUN mkdir -p /vboxguest && \
    cd /vboxguest && \
    \
    curl -L -o vboxguest.iso http://download.virtualbox.org/virtualbox/${VBOX_VERSION}/VBoxGuestAdditions_${VBOX_VERSION}.iso && \
    7z x vboxguest.iso -ir'!VBoxLinuxAdditions.run' && \
    \
    sh VBoxLinuxAdditions.run --noexec --target . && \
    mkdir -p amd64 && tar -C amd64 -xjf VBoxGuestAdditions-amd64.tar.bz2 && \
    \
    KERN_DIR=/usr/src/linux make -C amd64/src/vboxguest-${VBOX_VERSION}

ADD installer /installer
CMD /installer
