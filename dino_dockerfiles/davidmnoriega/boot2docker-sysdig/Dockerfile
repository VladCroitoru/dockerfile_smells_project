FROM boot2docker/boot2docker

# Build sysdig
ENV SYSDIG_REPO https://github.com/draios/sysdig.git
ENV SYSDIG_TAG 0.4.0

RUN apt-get update && apt-get -y install cmake && \
  git clone --branch "$SYSDIG_TAG" "$SYSDIG_REPO"  /sysdig && \
  mkdir /sysdig/build

WORKDIR /sysdig/build

RUN cmake -DCMAKE_BUILD_TYPE=Release -DSYSDIG_VERSION=$SYSDIG_TAG .. && \
  KERNELDIR=$ROOTFS/lib/modules/$KERNEL_VERSION-boot2docker/build make

RUN DESTDIR=$ROOTFS KERNELDIR=$ROOTFS/lib/modules/$KERNEL_VERSION-boot2docker/build make install && \
  cp driver/sysdig-probe.ko $ROOTFS/lib/modules/$KERNEL_VERSION-boot2docker && \
  depmod -a -b $ROOTFS $KERNEL_VERSION-boot2docker && \
  chmod u+s $ROOTFS/usr/local/bin/sysdig && \
  chmod u+s $ROOTFS/usr/local/bin/csysdig && \
  rm -rf /sysdig

WORKDIR /

RUN /make_iso.sh

CMD ["cat", "boot2docker.iso"]
