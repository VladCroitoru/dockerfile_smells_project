FROM ubuntu:14.04
MAINTAINER Benjamin Henrion <zoobab@gmail.com>

ENV user frosted

RUN DEBIAN_FRONTEND=noninteractive apt-get update -y -q
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q --force-yes build-essential git-core wget python pkg-config libglib2.0-dev zlib1g-dev libpixman-1-dev flex bison gdb-arm-none-eabi

RUN useradd -d /home/$user -m -s /bin/bash $user
RUN echo "$user ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/$user
RUN chmod 0440 /etc/sudoers.d/$user

USER $user

WORKDIR /home/$user
# todo: need to form the URL with some variables here
#ENV tbz2 arm-frosted-eabi-5.3.0_16.07.003.tar.bz2
ENV tbz2 arm-frosted-eabi-16.10.tar.bz2
RUN wget -O $tbz2 https://github.com/insane-adding-machines/crosstool-ng/releases/download/v16.10/$tbz2
RUN tar -xf $tbz2
RUN git clone https://github.com/insane-adding-machines/frosted
RUN cd frosted && git submodule init && git submodule update
RUN cd frosted/frosted-userland && git submodule init && git submodule update
ENV PATH /home/$user/arm-frosted-eabi/bin:$PATH

WORKDIR /home/$user/frosted
#RUN make defconfig TARGET=stm32f746-discovery
RUN wget https://git.io/vKgDR -O frosted-userland/kconfig/.config
RUN make defconfig TARGET=qemu
RUN make

USER $user
WORKDIR /home/$user

RUN git clone https://github.com/insane-adding-machines/qemu.git
WORKDIR /home/$user/qemu
RUN git submodule update --init dtc
RUN ./configure --prefix=`pwd`/../qemu-bin --target-list=arm-softmmu
RUN make 
RUN make install
ENV PATH /home/$user/qemu-bin/bin:$PATH

WORKDIR /home/$user
RUN git clone https://github.com/insane-adding-machines/micropython.git
RUN cd micropython && make -C mpy-cross

WORKDIR /home/$user/frosted
RUN make
#RUN cp micropython ~/frosted/frosted-userland/sh/

ENTRYPOINT ["qemu-system-arm","-semihosting","-M","lm3s6965evb","--kernel","/home/frosted/frosted/image.bin","-serial","stdio"]
