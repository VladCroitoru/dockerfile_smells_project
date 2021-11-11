FROM alpine:3.7

ENV BACKUP_COMMAND=/usr/local/bin/backup \
    BACKUP_LIFETIME=10 \
    BACKUP_PATH=/data/backup \
    BACKUP_PATTERN="+%Y-%m-%d-%H-%M-%S" \
    BACKUP_SCHEDULE="0 4 * * *"

VOLUME ${BACKUP_PATH}

RUN set -ex; \
# Install mongodb-tools
    apk add --no-cache mongodb-tools; \
# Remove unnecessary tools to reduce image size
    cd /usr/bin; \
    rm \
      bsondump \
      mongoexport \
      mongofiles \
      mongoimport \
      mongooplog \
      mongoreplay \
      mongostat \
      mongotop; \
# Download supercronic
    export \
      SUPERCRONIC_URL_ROOT=https://github.com/aptible/supercronic \
      SUPERCRONIC_URL_PATH=releases/download/v0.1.5/supercronic-linux-amd64 \
      SUPERCRONIC=/usr/bin/supercronic \
      SUPERCRONIC_SHA1SUM=9aeb41e00cc7b71d30d33c57a2333f2c2581a201; \
    \
    wget "${SUPERCRONIC_URL_ROOT}/${SUPERCRONIC_URL_PATH}" -O ${SUPERCRONIC}; \
    echo "${SUPERCRONIC_SHA1SUM}  ${SUPERCRONIC}" | sha1sum -c - ; \
    chmod +x "$SUPERCRONIC"


COPY ["scripts/*", "scripts/.*", "/usr/local/bin/"]
RUN chmod +x /usr/local/bin/* /usr/local/bin/.*

WORKDIR ${BACKUP_PATH}

CMD ["start-supercronic"]
