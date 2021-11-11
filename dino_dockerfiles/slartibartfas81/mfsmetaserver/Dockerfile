FROM alpine:latest
LABEL maintainer="uli@bruckdorfer-sr.de"
EXPOSE 9422

RUN addgroup mfs && adduser -S -D -H -G mfs mfs
RUN apk add --no-cache libgcc libstdc++ fuse
RUN mkdir -p /usr/local/etc/mfs/ && mkdir -p /usr/local/var/lib/mfs && chown mfs:mfs /usr/local/var/lib/mfs
COPY mfsmetalogger /usr/local/bin/mfsmetalogger
COPY mfsmetalogger.cfg /usr/local/mfsmetalogger.cfg

VOLUME /usr/local/var/lib/mfs/

ENV MFSM_MASTERHOST mfsmaster
ENV MFSM_BACKLOGS 24
ENV MFSM_DLFREQ 10

COPY entrypoint.sh ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
