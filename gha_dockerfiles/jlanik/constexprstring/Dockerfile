FROM rhub/fedora-clang

RUN dnf -y install git
RUN dnf install dnf-plugins-core
RUN dnf -y copr enable vbatts/bazel
RUN dnf -y install bazel4
RUN dnf -y install gdb
RUN dnf -y debuginfo-install glibc-2.32-10.fc33.x86_64 libgcc-10.3.1-1.fc33.x86_64 libstdc++-10.3.1-1.fc33.x86_64
