FROM alpine:latest
LABEL maintainer="uli@bruckdorfer-sr.de"
EXPOSE 9422

RUN addgroup mfs && adduser -S -D -H -G mfs mfs
RUN apk add --no-cache libgcc libstdc++ fuse
RUN mkdir -p /usr/local/etc/mfs/ && mkdir -p /usr/local/var/lib/mfs && chown mfs:mfs /usr/local/var/lib/mfs && mkdir -p /mnt/hdd
COPY mfschunkserver /usr/local/bin/mfschunkserver
COPY mfshdd.cfg.dist /usr/local/etc/mfs/mfshdd.cfg
COPY mfschunkserver.cfg.dist /usr/local/etc/mfs/mfschunkserver.cfg
VOLUME /mnt/hdd

ENV MFSM_MASTERHOST mfsmaster
ENV MFSC_LABEL _
ENV MFSC_LEAVE_SPACE 4GiB

COPY entrypoint.sh ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
