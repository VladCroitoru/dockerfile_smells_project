FROM alpine:latest
LABEL maintainer="uli@bruckdorfer-sr.de"
EXPOSE 9419 9420 9421 9424

RUN addgroup mfs && adduser -S -D -H -G mfs mfs
RUN apk add --no-cache libgcc libstdc++ fuse
RUN mkdir -p /usr/local/etc/mfs/ && mkdir -p /usr/local/var/lib/mfs && chown mfs:mfs /usr/local/var/lib/mfs && mkdir -p /usr/local/var/lib/mfs/
COPY mfsmaster /usr/local/bin/mfsmaster
COPY mfsmetarestore /usr/local/bin/mfsmetarestore
COPY mfsmaster.cfg /usr/local/mfsmaster.cfg
COPY mfsexports.cfg /usr/local/mfsexports.cfg
COPY mfsgoals.cfg /usr/local/mfsgoals.cfg
COPY mfstopology.cfg /usr/local/mfstopology.cfg
COPY metadata.mfs.empty /usr/local/metadata.mfs.empty
VOLUME /usr/local/var/lib/mfs
VOLUME /usr/local/etc/

ENV MFSM_PERSONALITY master
ENV MFSM_MASTERHOST mfsmaster
ENV MFSM_REBAL_LABELS 1
ENV MFSM_ACCEPT_DIFF 0.1

RUN touch /bootstrap
COPY entrypoint.sh ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
