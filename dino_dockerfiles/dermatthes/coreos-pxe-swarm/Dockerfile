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



# Select CoreOS Channel - currently we need alpha for testing (alpha supports docker 1.12)
ENV COREOS_CHANNEL alpha
# ENV COREOS_CHANNEL stable


COPY app /app
COPY oem /oem
RUN cd app/httpd && composer update


ADD download_coreos.sh /
RUN chmod 755 /download_coreos.sh
RUN /download_coreos.sh


#RUN cd /app/httpd ; rm -R ./vendor
# Install libraries





#     wget -q http://stable.release.core-os.net/amd64-usr/current/coreos_production_pxe.vmlinuz.sig && \
#     wget -q http://stable.release.core-os.net/amd64-usr/current/coreos_production_pxe_image.cpio.gz.sig && \
#     wget -qO- https://coreos.com/security/image-signing-key/CoreOS_Image_Signing_Key.pem | gpg --import && \
#     gpg --verify coreos_production_pxe.vmlinuz.sig && \
#     gpg --verify coreos_production_pxe_image.cpio.gz.sig


# Customizations
ENV INTERFACE=enp0s5
ENV INTERFACE_BOOTSTRAP=eth0
ENV MODE=BOOTSTRAP
ENV DEVMODE=0

ENV DHCP=0

# Default: use Proxy mode
ENV DHCP_RANGE=0
ENV NFS_MOUNT="10.16.0.1:/srv/nfs"


CMD /app/init
