FROM rbbratta/build-ubuntu-drivers-base
MAINTAINER ross.b.brattain@intel.com

RUN apt-get update && apt-get install -y --no-install-recommends \
        linux-image-extra-3.13.0-92-generic \
        linux-headers-3.13.0-92-generic \
    && apt-get clean


# -L for redirects
RUN curl -sS -L -o ixgbe-4.4.6.tar.gz 'http://downloads.sourceforge.net/project/e1000/ixgbe%20stable/4.4.6/ixgbe-4.4.6.tar.gz?use_mirror=heanet'  && tar -C /root -xvf ixgbe-4.4.6.tar.gz && rm ixgbe-4.4.6.tar.gz
RUN curl -sS -L -o i40e-1.5.19.tar.gz 'http://downloads.sourceforge.net/project/e1000/i40e%20stable/1.5.19/i40e-1.5.19.tar.gz?use_mirror=heanet'  && tar -C /root -xvf i40e-1.5.19.tar.gz && rm i40e-1.5.19.tar.gz


RUN make -C /root/ixgbe-4.4.6/src install BUILD_KERNEL=3.13.0-92-generic
RUN make -C /root/i40e-1.5.19/src install BUILD_KERNEL=3.13.0-92-generic


RUN mkdir /root/drivers
# use --transform to convert updates/ to kernel/ because bootstrap creator isn't grabbing modules from updates/
RUN tar --transform=s,^updates,kernel, --owner=root --group=root --numeric-owner -C /lib/modules/3.13.0-92-generic/ -cvzf /root/drivers/drivers-ubuntu-14.04-3.13.0-92-generic-i40e-1.5.19-ixgbe-4.4.6.tar.gz updates
ENTRYPOINT ["cp", "-rv", "/root/drivers", "/data"]
