FROM alpine:3.5
ENV \
  BASE_IMAGE=alpine:3.5 \
  LANG=C.UTF-8

RUN apk --update add ca-certificates curl && \
curl -fsSL https://raw.githubusercontent.com/elifarley/cross-installer/master/install.sh | sh && \
  xinstall add glibc && \
  xinstall save-image-info && \
  xinstall remove-pkg ca-certificates curl && \
  xinstall cleanup && \
  xinstall meta remove
