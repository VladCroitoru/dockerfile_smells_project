FROM ubuntu:14.04
MAINTAINER Benjamin Henrion <zoobab@gmail.com>

RUN apt-get update
RUN apt-get install -yy -q devscripts gcc-aarch64-linux-gnu wget device-tree-compiler bc git

ENV user pine64
RUN useradd -d /home/${user} -m -s /bin/bash ${user}
RUN echo "${user} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${user}
RUN chmod 0440 /etc/sudoers.d/${user}

USER ${user}
WORKDIR /home/${user}

ENV CROSS_COMPILE=aarch64-linux-gnu-

WORKDIR /home/${user}
RUN mkdir -pv ~/output

RUN git clone https://github.com/apritzel/arm-trusted-firmware.git
WORKDIR /home/$user/arm-trusted-firmware
RUN git checkout e70dd6ebe65d62d4d4d5873c3d2c900fe5633313
RUN make PLAT=sun50iw1p1 DEBUG=1 bl31
RUN cp build/sun50iw1p1/debug/bl31.bin ~/output

WORKDIR /home/${user}
ENV ubootversion u-boot-2016.11-rc3
RUN wget ftp://ftp.denx.de/pub/u-boot/${ubootversion}.tar.bz2
RUN tar -xf ${ubootversion}.tar.bz2

WORKDIR /home/${user}/${ubootversion}
RUN make pine64_plus_defconfig
RUN make
RUN cp u-boot.bin ~/output

WORKDIR /home/${user}
RUN git clone https://github.com/apritzel/pine64
WORKDIR /home/${user}/pine64/tools
RUN make boot0img
RUN cp boot0img ~/output/
RUN unxz --force ../images/pine64_firmware-20160601.img.xz
RUN dd if=../images/pine64_firmware-20160601.img of=boot0.bin bs=8k skip=1 count=4
RUN cp boot0.bin ~/output/

WORKDIR /home/${user}/output
RUN ./boot0img -B boot0.bin -s bl31.bin -a 0x44008 -d trampoline64:0x44000 -u u-boot.bin -e -p 100 -o pine64.img
