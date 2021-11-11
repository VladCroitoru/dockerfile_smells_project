FROM alpine:3.8

ENV GOPATH=/

RUN apk add --update openssl go ffmpeg make build-base opus-dev python aria2
RUN apk upgrade

RUN wget https://yt-dl.org/downloads/latest/youtube-dl -O /bin/youtube-dl && chmod a+x /bin/youtube-dl

COPY . /src/github.com/matthieugrieger/mumbledj
COPY config.yaml /root/.config/mumbledj/config.yaml

WORKDIR /src/github.com/matthieugrieger/mumbledj

RUN make
RUN make install
RUN apk del go make build-base && rm -rf /var/cache/apk/* && rm -rf /src

ENTRYPOINT ["/bin/sh", "-c", "/bin/youtube-dl -U && /usr/local/bin/mumbledj"]