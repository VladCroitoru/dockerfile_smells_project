FROM alpine

RUN apk add --no-cache --virtual=build-dependencies git cmake make gcc g++ libc-dev boost-dev && \
    git clone --recursive -b kost https://github.com/kost/nheqminer.git /nheqminer && \
    mkdir -p /nheqminer/nheqminer/build && \
    cd /nheqminer/nheqminer/build && \
    cmake -DSTATIC_BUILD=1 -DXENON=2 -DMARCH="-m64" .. && \
    make && \
    apk del --purge build-dependencies

# Metadata params
ARG BUILD_DATE
ARG VERSION
ARG VCS_URL
ARG VCS_REF
# Metadata
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="Kostminer" \
      org.label-schema.description="Running Kost version nheqminer in alpine docker container" \
      org.label-schema.url="https://github.com/kost/nheqminer.git" \
      org.label-schema.vcs-url=$VCS_URL \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vendor="AnyBucket" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0" \
      com.microscaling.docker.dockerfile="/Dockerfile"

ENTRYPOINT ["/nheqminer/nheqminer/build/nheqminer"]
