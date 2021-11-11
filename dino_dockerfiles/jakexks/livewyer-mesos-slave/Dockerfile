FROM progrium/busybox
MAINTAINER Jake Sanders <jake@livewyer.com>

RUN opkg-install curl bash wget ca-certificates
ADD consul-mesos-slave.sh /start
RUN chmod +x /start

ENTRYPOINT ["/start"]
CMD [""]
