ARG INFLUX_TAG=alpine

FROM influxdb:${INFLUX_TAG}

# OCI Meta information
LABEL org.opencontainers.image.authors="efrecon+github@gmail.com"
LABEL org.opencontainers.image.created=${BUILD_DATE}
LABEL org.opencontainers.image.version="1.1"
LABEL org.opencontainers.image.url="https://hub.docker.com/r/efrecon/influx-backup"
LABEL org.opencontainers.image.source="https://www.github.com/efrecon/influx-backup"
LABEL org.opencontainers.image.documentation="https://www.github.com/efrecon/influx-backup/README.md"
LABEL org.opencontainers.image.licenses="BSD-3-Clause"
LABEL org.opencontainers.image.title="efrecon/influx-backup"
LABEL org.opencontainers.image.description="Periodical or one-shot raw and CSV backups of Influx databases"

# Add base tcl distribution and copy backup script
RUN if command -v "apk" >/dev/null 2>&1; then apk --no-cache add tcl; fi && \
    if command -v "apt-get" >/dev/null 2>&1; then apt-get update -y && apt-get -y install tcl; fi
COPY backup.tcl /usr/local/bin/

# Export /backup volume which is the default root for backups.
VOLUME ["/backup"]

# Default entry point is backup, this easily skips any cmd/entrypoint that would
# inherit from the original influx image so no daemon is started or
# initialisation performed.
ENTRYPOINT ["tclsh8.6", "/usr/local/bin/backup.tcl"]