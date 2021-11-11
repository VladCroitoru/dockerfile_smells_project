FROM kinsamanka/docker-qemu-chroot:cross_compiler
MAINTAINER GP Orcullo <kinsamanka@gmail.com>

# download MK
ADD	https://github.com/kinsamanka/machinekit/archive/libm_fix.tar.gz \
		/opt/rootfs/usr/src/

# build MK
ADD	arm-linux-gnueabihf-* /opt/rootfs/usr/bin/
ADD	build_mk.sh /opt/rootfs/tmp/
RUN     proot -b /dev/shm -r /opt/rootfs -q qemu-arm-static /tmp/build_mk.sh

# default run command 
CMD	proot -b /dev/shm -r /opt/rootfs -q qemu-arm-static /bin/bash
