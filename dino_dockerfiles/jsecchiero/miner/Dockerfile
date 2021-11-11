FROM fedora:27
ENV container docker
RUN dnf -y update && dnf clean all
RUN dnf -y install systemd 
RUN dnf -y install libvirt-daemon-driver-* libvirt-daemon libvirt-daemon-kvm qemu-kvm \
                   qemu libvirt libvirt-devel ruby-devel gcc pciutils vagrant; \
                   dnf clean all; \
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

RUN mkdir -p /var/lib/libvirt/images/

# Edit the service file which includes ExecStartPost to chmod /dev/kvm
RUN sed -i "/Service/a ExecStartPost=\/bin\/chmod 666 /dev/kvm" /usr/lib/systemd/system/libvirtd.service

RUN dnf -y install virt-install virt-manager virt-viewer virt-what virt-who virt-top libvirt-daemon-config-network

RUN vagrant plugin install vagrant-libvirt
RUN vagrant box add jsecchiero/miner-amd --provider=libvirt --box-version=0.0.3

COPY vagrant.service /etc/systemd/system/
COPY vagrant-up /usr/local/sbin/
RUN chmod 554 /usr/local/sbin/vagrant-up && systemctl enable vagrant

COPY .  /var/lib/vagrant/
WORKDIR /var/lib/vagrant

VOLUME [ "/sys/fs/cgroup" ]
CMD ["/usr/sbin/init"]
