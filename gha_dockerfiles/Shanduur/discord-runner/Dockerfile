FROM golang:1.17 AS build

RUN apk add --no-cache \
        ca-certificates \
        git \
        make \
    ;

WORKDIR /tmp/
RUN git clone git@github.com:Shanduur/discord-runner.git

WORKDIR /tmp/discord-runner
RUN make build

FROM alpine:latest AS runtime

COPY --from=build /tmp/discord-runner/build/discord-runner /usr/bin/discord-runner

RUN chmod +x /usr/bin/discord-runner

ENTRYPOINT [ "/usr/bin/discord-runner" ]
