FROM ubuntu:xenial
MAINTAINER Mitchell Hewes <me@mitcdh.com>

# install prerequisites
RUN DEBIAN_FRONTEND=noninteractive \
 && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3FE869A9 \
 && echo "deb http://ppa.launchpad.net/gluster/nfs-ganesha/ubuntu xenial main" > /etc/apt/sources.list.d/nfs-ganesha.list \
 && echo "deb http://ppa.launchpad.net/gluster/libntirpc/ubuntu xenial main" > /etc/apt/sources.list.d/libntirpc.list \
 && apt-get update \
 && apt-get install -y wget unzip uuid-runtime python-setuptools udev runit sharutils nfs-common dbus nfs-ganesha nfs-ganesha-fsal \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
 && mkdir -p /run/rpcbind /export /var/run/dbus \
 && touch /run/rpcbind/rpcbind.xdr /run/rpcbind/portmap.xdr \
 && chmod 777 /run/rpcbind/* \
 && chown messagebus:messagebus /var/run/dbus

# Add startup script and ganesha config
ADD start.sh /
ADD ganesha.conf /etc/ganesha/ganesha.conf

# NFS ports and portmapper
EXPOSE 2049

# Start Ganesha NFS daemon by default
CMD ["/start.sh"]
