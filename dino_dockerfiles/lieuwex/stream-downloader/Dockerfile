FROM golang:1.16.3-alpine AS builder

WORKDIR /go/src/stream-downloader/
COPY . .
RUN go build -o /bin/stream-downloader

#####

FROM python:3-alpine AS runner

RUN apk update \
	&& apk add --no-cache \
		ffmpeg \
		tzdata \
		gcc \
		musl-dev \
		bash \
	&& pip install \
		streamlink \
	&& apk del --purge --force \
		linux-headers \
		binutils-gold \
		gnupg \
		zlib-dev \
		libc-utils \
		gcc \
		musl-dev \
	&& rm -rf /var/lib/apt/lists/* \
		/var/cache/apk/* \
		/usr/share/man \
		/tmp/*

# Copy convert script
COPY ./convert/convert /bin/convert

# Copy stream-downloader
COPY --from=builder /bin/stream-downloader /bin/stream-downloader

WORKDIR /root
CMD ["/bin/stream-downloader", "/root/"]
