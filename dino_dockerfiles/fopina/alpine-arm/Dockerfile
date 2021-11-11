# keeping duplicated Dockerfiles for now, until dockerhub upgrades to 1.9
# ARG CODE_VERSION 3.6
FROM arm32v6/alpine:3.6

ENV QEMU_EXECVE 1

COPY . /usr/bin

RUN [ "qemu-arm-static", "/bin/sh", "-c", "ln -s resin-xbuild /usr/bin/cross-build-start; ln -s resin-xbuild /usr/bin/cross-build-end; ln /bin/sh /bin/sh.real" ]
