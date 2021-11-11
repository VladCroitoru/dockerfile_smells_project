FROM golang:alpine as builder
RUN apk add --update git
RUN go get -u -v \
        -ldflags "-X main.version=$(curl -sSL https://api.github.com/repos/chenhw2/changeip-ddns-cli/commits/master | \
            sed -n '1,9{/sha/p; /date/p}' | sed 's/.* \"//g' | cut -c1-10 | tr [a-z] [A-Z] | sed 'N;s/\n/@/g')" \
        github.com/chenhw2/changeip-ddns-cli

FROM chenhw2/alpine:base
LABEL MAINTAINER CHENHW2 <https://github.com/chenhw2>

# /usr/bin/changeip-ddns-cli
COPY --from=builder /go/bin /usr/bin

USER nobody

ENV USERNAME=1234567890 \
    PASSWORD=abcdefghijklmn \
    DOMAIN=ddns.changeip.com \
    REDO=0

CMD changeip-ddns-cli \
    --username ${USERNAME} \
    --password ${PASSWORD} \
    auto-update \
    --domain ${DOMAIN} \
    --redo ${REDO}
