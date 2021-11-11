FROM debian:jessie
MAINTAINER GP Orcullo <kinsamanka@gmail.com>

# install required dependencies
RUN	apt-get update && \
	apt-get -y --no-install-recommends install \
		debootstrap \
		proot \
		qemu-user-static

# patch debootstrap as /proc cannot be mounted under proot
RUN	sed -i 's/in_target mount -t proc/#in_target mount -t proc/g' /usr/share/debootstrap/functions

# install native cross-compiler
ADD	http://emdebian.org/tools/debian/emdebian-toolchain-archive.key /tmp/
RUN	apt-key add /tmp/emdebian-toolchain-archive.key && \
	echo "deb http://emdebian.org/tools/debian/ jessie main" >> \
		/etc/apt/sources.list.d/emdebian.list && \
	dpkg --add-architecture armhf && \
	apt-get update && \
	apt-get install -y --no-install-recommends crossbuild-essential-armhf
