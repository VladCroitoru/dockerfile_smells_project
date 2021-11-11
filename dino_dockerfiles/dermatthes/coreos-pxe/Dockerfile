FROM ubuntu:16.04

MAINTAINER Matthias Leuffen <matthes@leuffen.de>

#RUN echo "deb http://vesta.informatik.rwth-aachen.de/ftp/pub/Linux/ubuntu/ubuntu/  trusty main restricted universe multiverse" > /etc/apt/sources.list && \
#echo "deb http://vesta.informatik.rwth-aachen.de/ftp/pub/Linux/ubuntu/ubuntu/  trusty-security main restricted universe multiverse" >> /etc/apt/sources.list && \
#echo "deb http://vesta.informatik.rwth-aachen.de/ftp/pub/Linux/ubuntu/ubuntu/ trusty-updates main restricted universe multiverse" >> /etc/apt/sources.list && \
#echo "deb http://vesta.informatik.rwth-aachen.de/ftp/pub/Linux/ubuntu/ubuntu/ trusty-proposed main restricted universe multiverse" >> /etc/apt/sources.list && \
#echo "deb http://vesta.informatik.rwth-aachen.de/ftp/pub/Linux/ubuntu/ubuntu/ trusty-backports main restricted universe multiverse" >> /etc/apt/sources.list

# Install deps
#RUN apt-get update && apt-get install -y dnsmasq pxelinux wget openssh-server openssh-client php7.0-cli php7.0-zip squashfs-tools composer cpio net-tools
RUN apt-get update && apt-get install -y dnsmasq pxelinux syslinux wget php7.0-cli php7.0-zip composer net-tools openssh-client

COPY app /app
COPY oem /oem


# Select CoreOS Channel - currently we need alpha for testing (alpha supports docker 1.12)
ENV COREOS_CHANNEL alpha
# ENV COREOS_CHANNEL stable


# Install pxelinux.0 AND ldlinux.c32 for network boot
RUN mkdir app/tftp && cp /usr/lib/PXELINUX/pxelinux.0 /app/tftp && cp /usr/lib/syslinux/modules/bios/ldlinux.c32 /app/tftp

# Import CoreOS Signing Key
RUN wget -qO- https://coreos.com/security/image-signing-key/CoreOS_Image_Signing_Key.pem | gpg --import

# Install coreos pxe images
RUN cd /app/tftp && \
    wget -q http://$COREOS_CHANNEL.release.core-os.net/amd64-usr/current/coreos_production_pxe.vmlinuz && \
    wget -q http://$COREOS_CHANNEL.release.core-os.net/amd64-usr/current/coreos_production_pxe.vmlinuz.sig && \
    gpg --verify coreos_production_pxe.vmlinuz.sig

# Download image to /tmp
RUN cd /tmp && \
    wget -q http://$COREOS_CHANNEL.release.core-os.net/amd64-usr/current/coreos_production_pxe_image.cpio.gz && \
    wget -q http://$COREOS_CHANNEL.release.core-os.net/amd64-usr/current/coreos_production_pxe_image.cpio.gz.sig && \
    gpg --verify coreos_production_pxe_image.cpio.gz.sig


# Extract and combine with /oem
#RUN mkdir /tmp/initrd && \
#    cd /tmp/initrd && \
#    cat /tmp/coreos_production_pxe_image.cpio.gz | gzip -d | cpio -i && \
#    unsquashfs -f -d ./tttmp usr.squashfs && \
#    cp -R /oem/* ./tttmp && \
#    rm usr.squashfs && \
#    mksquashfs ./tttmp ./usr.squashfs && \
#    rm -R ./tttmp && \
#    find | cpio -o --format=newc | gzip -9c > /app/tftp/coreos_production_pxe_image_oem.cpio.gz
RUN mv /tmp/coreos_production_pxe_image.cpio.gz /app/tftp/coreos_production_pxe_image_oem.cpio.gz

# Cleanup
RUN cd /tmp && rm -R *


#RUN cd /app/httpd ; rm -R ./vendor
# Install libraries

RUN cd /app/httpd && composer update




#     wget -q http://stable.release.core-os.net/amd64-usr/current/coreos_production_pxe.vmlinuz.sig && \
#     wget -q http://stable.release.core-os.net/amd64-usr/current/coreos_production_pxe_image.cpio.gz.sig && \
#     wget -qO- https://coreos.com/security/image-signing-key/CoreOS_Image_Signing_Key.pem | gpg --import && \
#     gpg --verify coreos_production_pxe.vmlinuz.sig && \
#     gpg --verify coreos_production_pxe_image.cpio.gz.sig


# Customizations
ENV INTERFACE=eth1

CMD /app/init
