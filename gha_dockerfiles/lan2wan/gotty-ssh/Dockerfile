FROM --platform=${BUILDPLATFORM} alpine:3.14 as builder

ARG TARGETOS
ARG TARGETARCH
ARG GOTTY_VERSION="v1.3.0"

COPY scripts/get_gotty.sh /get_gotty.sh
RUN chmod +x /get_gotty.sh && /get_gotty.sh


FROM alpine:3.14

LABEL maintainer="Jeeva Kandasamy <jkandasa@gmail.com>"

EXPOSE 8080

# install bash utils
RUN apk --no-cache add openssh-client libc6-compat && \
    mkdir /app

COPY --from=builder /gotty /app/gotty

RUN adduser --disabled-password --uid 1001 --no-create-home gottyuser

USER 1001

ENTRYPOINT [ "/app/gotty" ]

CMD ["-p", "8080", "-w", "/bin/sh"]
