FROM alpine:3

RUN apk update && apk add --no-cache libstdc++ libgcc

RUN mkdir -p /opt/refactr
WORKDIR /opt/refactr

COPY ./dist/refactrctl-alpine ./bin/refactrctl
RUN chmod +x ./bin/refactrctl

ENV PATH="/opt/refactr/bin:${PATH}"

ENTRYPOINT ["./bin/refactrctl"]
