# syntax = tonistiigi/dockerfile:runmount20180925

ARG BASE_CROSS=tonistiigi/copy:base@sha256:2d78a3d235897ed8de91a455cdd8270ebe532dbb78382c944a927e98a88f9c4d

# xcross wraps go to automatically configure TARGETPLATFORM 
FROM --platform=$BUILDPLATFORM tonistiigi/xx:golang@sha256:41b391dde0c3046c859b0247cd42eb53b4cea346ac5de0f047f24f56156762d0 AS xcross

FROM --platform=$BUILDPLATFORM golang:1.11 AS main
RUN apt-get update && apt-get install -y file
COPY --from=xcross / /
WORKDIR /go/src/github.com/tonistiigi/copy
ARG TARGETPLATFORM
RUN --mount=target=. --mount=target=/root/.cache,type=cache \
  CGO_ENABLED=0 go build -o /copy -ldflags '-s -w' github.com/tonistiigi/copy/cmd/copy && \
  file /copy | grep "statically linked"


FROM gruebel/upx@sha256:99891d91d6e409ad0dcdb4c70839f105ebf20421bebf896bfc4df827d5a8b19e AS upx
COPY --from=main /copy /copy
RUN ["upx", "/copy"]

FROM alpine AS rootfs
RUN mkdir -p /out/etc/apk && cp -r /etc/apk/* /out/etc/apk/
RUN apk add --no-cache --initdb -p /out tar gzip bzip2 xz
RUN rm -rf /out/etc/apk /out/lib/apk /out/var/cache

FROM scratch AS base-inline
COPY --from=rootfs /out/ /

# amd64 and !amd64 can use different sources
FROM upx AS source-amd64
FROM main AS source-arm
FROM main AS source-arm64
FROM main AS source-s390x
FROM main AS source-ppc64le
FROM source-$TARGETARCH AS source

# allow different modes of getting base image 
FROM base-inline AS base-amd64-amd64
FROM base-inline AS base-arm-arm
FROM base-inline AS base-arm64-arm64
FROM base-inline AS base-s390x-s390x
FROM base-inline AS base-ppc64le-ppc64le
FROM $BASE_CROSS AS base-amd64-arm 
FROM $BASE_CROSS AS base-amd64-arm64
FROM $BASE_CROSS AS base-amd64-s390x
FROM $BASE_CROSS AS base-amd64-ppc64le
FROM base-$BUILDARCH-$TARGETARCH AS base

# main release stage
FROM base AS release
COPY --from=source /copy /bin/
ENTRYPOINT ["/bin/copy"]

# dev image stage for debugging
FROM alpine AS dev-env
COPY --from=source /copy /bin/
ENTRYPOINT ["ash"]

# set default back to release
FROM release
