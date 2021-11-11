# To set multiarch build for Docker hub automated build.
FROM --platform=$TARGETPLATFORM golang:alpine AS builder
ARG TARGETPLATFORM
ARG BUILDPLATFORM

WORKDIR /go
RUN apk add git curl perl --no-cache

RUN set -eux; \
    \
	sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories; \
	sed -i 's/uk.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories; \
	apk --no-cache --no-progress upgrade; \
	buildDeps=' \
		build-base \
		git \
    '; \
    \
    apk add --no-cache --virtual .build-deps \
		$buildDeps \
	; \
    \
    git clone --depth 1 https://github.com/badafans/better-cloudflare-ip; \
    cd better-cloudflare-ip; \
    # apply a unmerged pull request
    curl https://github.com/badafans/better-cloudflare-ip/commit/b6a1c0253a525a2dab0e752dae1947019d55688c.patch -o 49.patch; \
    git apply --check 49.patch && git apply 49.patch; \
    \
    cd linux; \
    sed -i -E "s/read -p .* bandwidth$/bandwidth=\$\{BANDWIDTH:-20\}/" ./src/cf.sh; \
    sed -i -E "s/update\.freecdn\.workers\.dev/cfip\.pages\.dev/g" ./src/cf.sh; \
    sed -i -E "s/\ *\.\/fping */fping /" ./src/cf.sh; \
    echo -e '\n        echo $anycast > /data/ip.txt' >> ./src/cf.sh; \
    echo -e '\n        env |grep GIST_ &>1 && gist.sh /data/ip.txt' >> ./src/cf.sh; \
    \
    chmod +x ./configure; \
    ./configure; \
    make

FROM --platform=$TARGETPLATFORM alpine AS runtime
ARG TARGETPLATFORM
ARG BUILDPLATFORM
ENV BANDWIDTH=20

COPY --from=builder /go/better-cloudflare-ip/linux/src/fping /usr/local/bin/
COPY --from=builder /go/better-cloudflare-ip/linux/src/cf.sh /usr/local/bin/
COPY entrypoint.sh /usr/local/bin/
COPY gist.sh /usr/local/bin/

RUN set -eux; \
    \
    apk add --no-cache \
        bash \
        curl \
		ca-certificates \
	; \
    chmod +x /usr/local/bin/*; \
    echo "0 */6 * * * /usr/bin/flock -n /tmp/fcj.lockfile /usr/local/bin/cf.sh > /proc/1/fd/1 2>/proc/1/fd/2" > /etc/crontabs/root;

VOLUME [ "/data" ]

WORKDIR /

ENTRYPOINT [ "entrypoint.sh" ]
CMD ["crond", "-f", "-d", "8"]
