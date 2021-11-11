ARG VERSION=1.0.0

FROM golang:1-buster AS builder
RUN apt update && apt install -y git bash wget gcc make

ARG VERSION

RUN wget -O - "https://api.github.com/repos/XTLS/Xray-core/releases/latest" \
    | grep "tarball_url" | cut -d\" -f4 \
    | wget -O /tmp/xray.tar.gz -i -

ENV WD=/tmp/xray
RUN mkdir -p "$WD"
RUN tar -zxvf /tmp/xray.tar.gz --strip-components=1 -C "$WD" && cd "$WD" \
    && CGO_ENABLED=0 go build -o xray -trimpath -ldflags "-s -w -buildid=" ./main
RUN chmod +x "$WD/xray"
RUN wget -O "$WD/geoip.dat" "https://github.com/v2fly/geoip/raw/release/geoip.dat"
RUN wget -O "$WD/geosite.dat" "https://github.com/v2fly/domain-list-community/raw/release/dlc.dat"

FROM gcr.io/distroless/static

COPY --from=builder /tmp/xray/xray /usr/local/bin/
COPY --from=builder /tmp/xray/geo* /usr/local/bin/

CMD ["/usr/local/bin/xray", "-config", "/usr/local/etc/xray/config.json"]
