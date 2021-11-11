FROM alpine:3.12
ARG CED_VERSION
ARG TARGETARCH
ARG TARGETVARIANT
RUN apk update && apk add --no-cache ca-certificates && addgroup -S ced && adduser -S ced -G ced
ADD https://github.com/blmhemu/ced/releases/download/v${CED_VERSION}/ced_${CED_VERSION}_linux_${TARGETARCH}${TARGETVARIANT} /usr/bin/ced
ADD ced.properties /etc/ced/ced.properties
RUN chmod +x /usr/bin/ced && chmod +r /etc/ced/ced.properties
USER ced
ENTRYPOINT ["/usr/bin/ced"]
CMD ["-cfg", "/etc/ced/ced.properties"]
