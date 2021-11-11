FROM concourse/concourse:latest as cache

FROM alpine:edge as downloader
RUN apk add --no-cache curl jq
RUN url=$(curl -s "https://api.github.com/repos/concourse/concourse/releases/latest" \
    | jq -r '.assets[] | select(.name | test("fly.*linux.*amd64.tgz$")) | .browser_download_url') && \
    curl -L "$url" -o /fly.tgz && tar -xvf /fly.tgz

FROM alpine:edge
RUN apk add --no-cache bash tzdata ca-certificates
COPY --from=downloader /fly /usr/local/bin/fly
RUN chmod +x /usr/local/bin/fly
