FROM golang:1.7-alpine as build_go
COPY cross-build.go /cross-build/cross-build.go
WORKDIR /cross-build
RUN go build -ldflags "-w -s" cross-build.go

#------------------------------------------

FROM debian:jessie as build_base
# Add Backports repo support
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >>/etc/apt/sources.list
RUN echo "deb-src http://ftp.debian.org/debian jessie-backports main" >>/etc/apt/sources.list

# Install all required development packages
RUN apt-get -y update && apt-get -y build-dep qemu
RUN apt-get -y install git ca-certificates

# Clone a fork of QEMU that supports permanent EXECVE ( see https://resin.io/blog/building-arm-containers-on-any-x86-machine-even-dockerhub/ )
RUN git clone https://github.com/resin-io/qemu.git /qemu
WORKDIR /qemu
RUN git checkout resin-2.9.0

#------------------------------------------

FROM build_base as build_x86_64
# setup arch directory
RUN mkdir -p /cross-build/x86_64/bin
WORKDIR /cross-build/x86_64/bin
RUN echo "#!/bin/sh" >cross-build-start && chmod +x cross-build-start
RUN echo "#!/bin/sh" >cross-build-end && chmod +x cross-build-end

#------------------------------------------

FROM build_base as build_arm64v8
# Build the qemu binaries
RUN mkdir build
WORKDIR /qemu/build
RUN ../configure --disable-bsd-user --disable-guest-agent --disable-strip --disable-werror \
      --disable-gcrypt --disable-debug-info --disable-debug-tcg --enable-docs \
      --disable-tcg-interpreter --enable-attr --disable-brlapi --disable-linux-aio \
      --disable-bzip2 --disable-bluez --disable-cap-ng --disable-curl --disable-fdt \
      --disable-glusterfs --disable-gnutls --disable-nettle --disable-gtk --disable-rdma \
      --disable-libiscsi --disable-vnc-jpeg --disable-kvm --disable-lzo --disable-curses \
      --disable-libnfs --disable-numa --disable-opengl --disable-vnc-png --disable-rbd \
      --disable-vnc-sasl --disable-sdl --disable-seccomp --disable-smartcard --disable-snappy \
      --disable-spice --disable-libssh2 --disable-libusb --disable-usb-redir --disable-vde \
      --disable-vhost-net --disable-virglrenderer --disable-virtfs --disable-vnc \
      --disable-vte --disable-xen --disable-xen-pci-passthrough --disable-xfsctl \
      --enable-linux-user --disable-system --disable-blobs --disable-tools --disable-pie \
      --target-list=aarch64-linux-user --static
RUN make

# setup arch directory
RUN mkdir -p /cross-build/arm64v8/bin
WORKDIR /cross-build/arm64v8/bin
COPY --from=build_go /cross-build/cross-build /cross-build/arm64v8/bin/cross-build
RUN ln -s cross-build cross-build-start
RUN ln -s cross-build cross-build-end
RUN cp /qemu/build/aarch64-linux-user/qemu-aarch64 /cross-build/arm64v8/bin/qemu-static

#------------------------------------------

FROM build_base as build_arm32v7
# Build the qemu binaries
RUN mkdir build
WORKDIR /qemu/build
RUN ../configure --disable-bsd-user --disable-guest-agent --disable-strip --disable-werror \
      --disable-gcrypt --disable-debug-info --disable-debug-tcg --enable-docs \
      --disable-tcg-interpreter --enable-attr --disable-brlapi --disable-linux-aio \
      --disable-bzip2 --disable-bluez --disable-cap-ng --disable-curl --disable-fdt \
      --disable-glusterfs --disable-gnutls --disable-nettle --disable-gtk --disable-rdma \
      --disable-libiscsi --disable-vnc-jpeg --disable-kvm --disable-lzo --disable-curses \
      --disable-libnfs --disable-numa --disable-opengl --disable-vnc-png --disable-rbd \
      --disable-vnc-sasl --disable-sdl --disable-seccomp --disable-smartcard --disable-snappy \
      --disable-spice --disable-libssh2 --disable-libusb --disable-usb-redir --disable-vde \
      --disable-vhost-net --disable-virglrenderer --disable-virtfs --disable-vnc \
      --disable-vte --disable-xen --disable-xen-pci-passthrough --disable-xfsctl \
      --enable-linux-user --disable-system --disable-blobs --disable-tools --disable-pie \
      --target-list=arm-linux-user --static
RUN make

# setup arch directory
RUN mkdir -p /cross-build/arm32v7/bin
WORKDIR /cross-build/arm32v7/bin
COPY --from=build_go /cross-build/cross-build /cross-build/arm32v7/bin/cross-build
RUN ln -s cross-build cross-build-start
RUN ln -s cross-build cross-build-end
RUN cp /qemu/build/arm-linux-user/qemu-arm /cross-build/arm32v7/bin/qemu-static

#------------------------------------------
# Build the actual image:
# lets use alpine so we have a minimal environment we can use to poke around in
FROM alpine:latest
# copy our architecture directories
COPY --from=build_x86_64 /cross-build /cross-build
COPY --from=build_arm32v7 /cross-build /cross-build
COPY --from=build_arm64v8 /cross-build /cross-build
