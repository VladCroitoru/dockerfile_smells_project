FROM justincormack/rumprun-nginx-lua

MAINTAINER Justin Cormack <justin@specialbusservice.com>

COPY . /usr/src/rump-nginx-lua-test

WORKDIR /usr/src/rump-nginx-lua-test

RUN \
  genisoimage -l -r -o etc.iso etc && \
  genisoimage -l -r -o data.iso data
 
CMD rumprun qemu -i -I 'qnet0,vioif,-net tap,ifname=tap0' -W qnet0,inet,dhcp -b etc.iso,/etc -b data.iso,/data /usr/local/bin/nginx.hw_virtio -- -c /data/conf/nginx.conf
