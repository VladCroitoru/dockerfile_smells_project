FROM        progrium/busybox
MAINTAINER  Fletcher Nichol <fnichol@nichol.ca>

# provide /etc/ssl/certs/ca-certificates.crt to container
RUN opkg-install ca-certificates
RUN for cert in `ls -1 /etc/ssl/certs/*.crt | grep -v /etc/ssl/certs/ca-certificates.crt`; do cat "$cert" >> /etc/ssl/certs/ca-certificates.crt; done

ADD https://github.com/fnichol/tapasd/releases/download/v0.1.0/tapasd_linux_amd64 /bin/tapasd
RUN chmod +x /bin/tapasd

VOLUME ["/data"]

ENTRYPOINT ["/bin/tapasd", "-data=/data"]
