FROM fedora:28

RUN dnf -y install \
    gcc gcc-c++ cmake git make \
    mesa-libGL-devel \
    libXrandr-devel \
    libXinerama-devel \
    libXcursor-devel \
    libXi-devel \
    mingw64-gcc \
    mingw64-gcc-c++ \
    mingw64-winpthreads-static \
    mingw32-gcc \
    mingw32-gcc-c++ \
    mingw32-winpthreads-static \
  && dnf clean all

