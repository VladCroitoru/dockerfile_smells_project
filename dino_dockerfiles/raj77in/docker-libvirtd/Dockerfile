FROM fedora
MAINTAINER "Amit Agarwal" 
ENV container docker
RUN dnf -y update && dnf clean all
# RUN rpm -e --nodeps fakesystemd
RUN dnf -y install systemd 
#RUN dnf -y install libvirt-daemon-driver-{network,interface,storage,qemu} qemu systemd libvirt-daemon && dnf clean all; \
RUN dnf -y install libvirt-daemon-driver-* libvirt-daemon libvirt-daemon-kvm qemu-kvm && dnf clean all; \
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*; \
systemctl enable libvirtd; \
systemctl enable virtlockd 

EXPOSE 16509

RUN echo "listen_tls = 0" >> /etc/libvirt/libvirtd.conf; \
echo 'listen_tcp = 1' >> /etc/libvirt/libvirtd.conf; \
echo 'tls_port = "16514"' >> /etc/libvirt/libvirtd.conf; \ 
echo 'tcp_port = "16509"' >> /etc/libvirt/libvirtd.conf; \
echo 'auth_tcp = "none"' >> /etc/libvirt/libvirtd.conf

RUN echo 'LIBVIRTD_ARGS="--listen"' >> /etc/sysconfig/libvirtd
RUN mkdir -p /var/lib/libvirt/images/

# Edit the service file which includes ExecStartPost to chmod /dev/kvm
RUN sed -i "/Service/a ExecStartPost=\/bin\/chmod 666 /dev/kvm" /usr/lib/systemd/system/libvirtd.service

RUN dnf -y install virt-install virt-manager virt-viewer virt-what virt-who virt-top libvirt-daemon-config-network

VOLUME [ "/sys/fs/cgroup" ]
CMD ["/usr/sbin/init"]
