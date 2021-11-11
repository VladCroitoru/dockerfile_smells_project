FROM centos:8
LABEL maintainer "Alexis Jeandet <alexis.jeandet@member.fsf.org>"


RUN dnf install -y --nogpgcheck https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm \
        && dnf install -y  --nogpgcheck https://mirrors.rpmfusion.org/free/el/rpmfusion-free-release-8.noarch.rpm https://mirrors.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-8.noarch.rpm\
        && dnf install -y 'dnf-command(config-manager)' \
        && dnf config-manager --enable powertools \
        && dnf install -y --nodocs --setopt install_weak_deps=False https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm git cppcheck bzip2 hg automake autoconf gcc glibc.i686 /lib/ld-linux.so.2 zlib.i686 ncurses-compat-libs.i686 cmake gcc-c++ tcl /bin/find xz make python3-pip python3-devel \
        && pip3 install meson ninja numpy ddt \
	&& dnf clean all -y


ADD https://hephaistos.lpp.polytechnique.fr/data/mirrors/gaisler/rcc/bin/linux/sparc-rtems-4.10-gcc-4.4.6-1.2.25-linux.tar.bz2 /opt/
ADD https://hephaistos.lpp.polytechnique.fr/data/mirrors/gaisler/rcc/src/rtems-4.10-1.2.25-src.tar.bz2 /opt/
ADD https://www.mjr19.org.uk/sw/inode64.so /usr/lib/

RUN g++ -shared -Wl,-soname -o  /usr/lib64/inode64.so && ldconfig -v 

ENV LD_PRELOAD=inode64.so

RUN cd /opt && tar -xf /opt/sparc-rtems-4.10-gcc-4.4.6-1.2.25-linux.tar.bz2 && \
    cd /opt/rtems-4.10/src && tar -xf /opt/rtems-4.10-1.2.25-src.tar.bz2 && \
    sed -i '0,/grspw_hw_reset(pDev);/s/grspw_hw_reset(pDev);/\/\/grspw_hw_reset(pDev);/' /opt/rtems-4.10/src/rtems-4.10/c/src/lib/libbsp/sparc/shared/spw/grspw.c && \
    /opt/rtems-4.10/bin/sparc-rtems-gcc -v && \
    /opt/rtems-4.10/bin/sparc-rtems-ld -v && \
    /opt/rtems-4.10/bin/sparc-rtems-g++ -v && \
    /opt/rtems-4.10/bin/sparc-rtems-objdump -v && \
    make -j bootstrap && \
    make -j bootstrap_sparc && \
    make -j configure-drvmgr && \
    make -j compile-drvmgr && \
    make -j install-drvmgr && \
    rm -f /opt/sparc-rtems-4.10-gcc-4.4.6-1.2.25-linux.tar.bz2 /opt/rtems-4.10-1.2.25-src.tar.bz2



