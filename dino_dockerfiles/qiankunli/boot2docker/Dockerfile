# using VirtualBox Guest Additions & FIG

FROM boot2docker/boot2docker

# Set this to your Virtual Box Version
ENV VBOXVER 4.3.14
# This is the name of Virtual Box Share to Automount
ENV VBOXSHARENAME home
# This is the path in the boot2docker guest where the share will mount
ENV VBOXSHAREGUESTPATH /home/docker/code

# config your http_proxy

RUN apt-get install p7zip-full

RUN mkdir -p /vboxguest && \
    cd /vboxguest && \
    curl -L -o vboxguest.iso http://download.virtualbox.org/virtualbox/$VBOXVER/VBoxGuestAdditions_$VBOXVER.iso && \
    7z x vboxguest.iso -ir'!VBoxLinuxAdditions.run' && \
    sh VBoxLinuxAdditions.run --noexec --target . && \
    mkdir x86 && cd x86 && tar xvjf ../VBoxGuestAdditions-x86.tar.bz2 && cd .. && \
    mkdir amd64 && cd amd64 && tar xvjf ../VBoxGuestAdditions-amd64.tar.bz2 && cd .. && \
    cd amd64/src/vboxguest-$VBOXVER && KERN_DIR=/linux-kernel/ make && cd ../../.. && \
    cp amd64/src/vboxguest-$VBOXVER/*.ko $ROOTFS/lib/modules/$KERNEL_VERSION-tinycore64 && \
    mkdir -p $ROOTFS/sbin && cp x86/lib/VBoxGuestAdditions/mount.vboxsf $ROOTFS/sbin/

RUN echo "" >> $ROOTFS/etc/motd; \
    echo "  boot2docker with VirtualBox guest additions version $VBOXVER with Fig 0.5.2" >> $ROOTFS/etc/motd; \
    echo "" >> $ROOTFS/etc/motd

# make mount permanent @todo it works, but its ugly. where should this go?
RUN echo '#!/bin/sh' >> $ROOTFS/etc/rc.d/vbox-guest-additions-permanent-mount; \
    echo 'sudo modprobe vboxsf && sudo mkdir $VBOXSHAREGUESTPATH && sudo mount -t vboxsf $VBOXSHARENAME $VBOXSHAREGUESTPATH' >> $ROOTFS/etc/rc.d/vbox-guest-additions-permanent-mount
RUN chmod +x $ROOTFS/etc/rc.d/vbox-guest-additions-permanent-mount
RUN echo '/etc/rc.d/vbox-guest-additions-permanent-mount' >> $ROOTFS/opt/bootsync.sh

# FIG install
# RUN curl -L https://github.com/docker/fig/releases/download/0.5.2/linux > $ROOTFS/usr/local/bin/fig
# RUN chmod +x $ROOTFS/usr/local/bin/fig

# Add TCZ Extensions
RUN tczex="python python-distribute" &&\
    for dep in $tczex; do \
      echo "Download $TCL_REPO_BASE/tcz/$dep.tcz" &&\
      curl -L -o /tmp/$dep.tcz $TCL_REPO_BASE/tcz/$dep.tcz && \
      unsquashfs -f -d $ROOTFS /tmp/$dep.tcz && \
      rm -f /tmp/$dep.tcz;\
    done

# This is very hackish, and a smarter person would do better to not use this method
# This has a high probability of breaking in the future as python and python-distribute tcz packages update!
ADD python/site-packages/ $ROOTFS/usr/local/lib/python2.7/site-packages/
ADD python/bin/ $ROOTFS/usr/local/bin/
#RUN chmod +x $ROOTFS/usr/local/bin/*

# config timezone
RUN sed -i "s#append loglevel=3 user=docker console=ttyS0 console=tty0 noembed nomodeset norestore waitusb=10:LABEL=boot2docker-data base#append tz=CST-8 loglevel=3 user=docker console=ttyS0 console=tty0 noembed nomodeset norestore waitusb=10:LABEL=boot2docker-data base#g" /isolinux/isolinux.cfg

RUN depmod -a -b $ROOTFS $KERNEL_VERSION-tinycore64
RUN /make_iso.sh
CMD ["cat", "boot2docker.iso"]
