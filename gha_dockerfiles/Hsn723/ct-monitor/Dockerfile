FROM golang:1.17.3-buster as build
ARG ARCH=amd64
ENV CGO_ENABLED=0
WORKDIR /work
RUN mkdir -p /etc/ct-monitor /var/log/ct-monitor \
    && chown nobody:nogroup /etc/ct-monitor /var/log/ct-monitor


FROM scratch
LABEL org.opencontainers.image.authors="Hsn723" \
      org.opencontainers.image.title="ct-monitor" \
      org.opencontainers.image.source="https://github.com/hsn723/ct-monitor"
COPY --from=build /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
COPY --from=build /etc/passwd /etc/passwd
COPY --from=build /etc/group /etc/group
COPY --from=build --chown=nobody:nogroup /etc/ct-monitor /etc/ct-monitor
COPY --from=build --chown=nobody:nogroup /var/log/ct-monitor /var/log/ct-monitor
COPY LICENSE /LICENSE
COPY ct-monitor /

USER 65534:65534

ENTRYPOINT [ "/ct-monitor" ]
