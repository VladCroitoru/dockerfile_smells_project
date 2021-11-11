FROM ubuntu:bionic
MAINTAINER George Kutsurua <g.kutsurua@gmail.com>

RUN apt update && apt upgrade -y &&\
    DEBIAN_FRONTEND=noninteractive \
        apt install -y glusterfs-server glusterfs-client attr rsync tar sudo xfsprogs \
                       thin-provisioning-tools lvm2 && \
    # Configure LVM to create LVs and snapshots
    sed -i.save -e "s#udev_sync = 1#udev_sync = 0#" \
        -e "s#udev_rules = 1#udev_rules = 0#" \
        -e "s#use_lvmetad = 1#use_lvmetad = 0#" /etc/lvm/lvm.conf && \
    apt -y clean

COPY ["entrypoint.sh", "/"]

VOLUME ["/var/lib/glusterd"]

# For client communication 49152-49251
EXPOSE 24007

ENTRYPOINT /entrypoint.sh
CMD ""