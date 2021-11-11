FROM progrium/busybox
MAINTAINER Jake Sanders <jake@livewyer.com>

RUN opkg-install curl bash wget ca-certificates
ADD consul-marathon.sh /start
RUN chmod +x /start

ENTRYPOINT ["/start"]
CMD [""]
