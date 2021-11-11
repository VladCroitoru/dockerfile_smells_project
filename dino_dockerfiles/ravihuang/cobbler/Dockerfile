FROM centos:7
MAINTAINER Ravi Huang <ravi.huang@gmail.com>

VOLUME /sys/fs/cgroup /run /tmp /mnt/cdrom
ENV container=docker

RUN yum -y install curl epel-release pykickstart dhcp
RUN yum -y install cobbler cobbler-web fence-agents xinetd  && yum update -y --enablerepo=epel-testing cobbler && \
    sed -i -e 's/\(^.*disable.*=\) yes/\1 no/' /etc/xinetd.d/tftp && \
    sed -i -e 's/manage_dhcp: 0/manage_dhcp: 1/' /etc/cobbler/settings && \
    sed -i -e 's/manage_rsync: 0/manage_rsync: 1/' /etc/cobbler/settings && \
    (echo -n "cobbler:Cobbler:" && echo -n "cobbler:Cobbler:passwd" | md5sum | awk '{print $1}' ) >/etc/cobbler/users.digest && \
    rm -f /var/lib/cobbler/loaders/* && yum clean all 

RUN cd /tmp && \
    curl -O http://ftp.es.debian.org/debian/pool/main/d/debmirror/debmirror_2.25.tar.xz && \
    tar xf debmirror_2.25.tar.xz && \
    cp debmirror/debmirror /usr/bin/ && \
    rm -rf debmirror*

ADD setenv /
RUN chmod +x /setenv

CMD ["/usr/sbin/init"]

EXPOSE 25151
EXPOSE 69/udp
EXPOSE 80
EXPOSE 443

