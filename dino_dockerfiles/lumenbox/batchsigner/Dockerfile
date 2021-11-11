FROM centos as builder

ENV SUPERCRONIC_URL=https://github.com/aptible/supercronic/releases/download/v0.1.5/supercronic-linux-amd64 \
    SUPERCRONIC=supercronic-linux-amd64 \
    SUPERCRONIC_SHA1SUM=9aeb41e00cc7b71d30d33c57a2333f2c2581a201

RUN curl -fsSLO "$SUPERCRONIC_URL" \
 && echo "${SUPERCRONIC_SHA1SUM}  ${SUPERCRONIC}" | sha1sum -c - \
 && chmod +x "$SUPERCRONIC" \
 && mv "$SUPERCRONIC" "/usr/local/bin/supercronic"

WORKDIR /tmp/
ARG CONFD_VERSION=0.15.0
ADD https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-amd64 /confd
COPY docker/confd /etc/confd
RUN chmod 755 /confd && \
    chmod 755 /etc/confd/confd-wrapper.sh



FROM python:2-alpine

WORKDIR /usr/src/app

COPY docker/requirements.txt ./

RUN apk --update --no-cache add ca-certificates bash postgresql-libs libffi && \
    apk --update --no-cache add --virtual .build-deps gcc postgresql-dev musl-dev libffi-dev make && \
    pip install --no-cache-dir -r requirements.txt && \
    apk --purge del .build-deps

COPY batchsigner.py log.py sshtunnel.py  ./
ADD federationxdr federationxdr

COPY --from=builder /usr/local/bin/supercronic /confd /
COPY --from=builder /etc/confd /etc/confd

CMD ["/etc/confd/confd-wrapper.sh"]
