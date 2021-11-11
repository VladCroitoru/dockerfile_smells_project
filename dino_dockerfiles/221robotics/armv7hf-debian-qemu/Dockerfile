FROM resin/armv7hf-debian:jessie

ENV QEMU_EXECVE 1

COPY . /usr/bin

RUN [ "qemu-arm-static", "/bin/sh", "-c", "ln -nsf resin-xbuild /usr/bin/cross-build-start; ln -nsf resin-xbuild /usr/bin/cross-build-end; ln /bin/sh /bin/sh.real" ]
