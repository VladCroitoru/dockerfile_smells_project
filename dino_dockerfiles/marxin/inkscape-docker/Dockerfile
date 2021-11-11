FROM marxin/gcc-docker
MAINTAINER Martin Liška

WORKDIR /abuild/inkscape
ENV CFLAGS -flto=4
ENV CXXFLAGS -flto=4
ENV LDFLAGS -flto=4

RUN echo "CPUs: `nproc`" && echo "MEMORY: " `cat /proc/meminfo | grep MemTotal` && cat /proc/cpuinfo | tail -n50 && df -h

RUN ./configure && make -j$(nproc) V=1
