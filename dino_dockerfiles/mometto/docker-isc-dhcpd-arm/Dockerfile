FROM resin/armv7hf-debian-qemu as builder

RUN [ "cross-build-start" ]

RUN apt-get update \
 && apt-get upgrade -y \
 && apt-get install -y isc-dhcp-server \
 && rm -rf /var/lib/apt/lists/*

RUN touch /var/lib/dhcp/dhcpd.leases

RUN [ "cross-build-end" ]  

FROM alpine:latest  

COPY --from=builder /usr/sbin/dhcpd /usr/sbin/dhcpd

VOLUME ["/var/lib/dhcp", "/etc/dhcp"]

ENTRYPOINT ["/usr/sbin/dhcpd", "-d", "--no-pid"]

