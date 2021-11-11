FROM alpine:3.5
MAINTAINER Volker Machon <volker@machon.biz>

RUN addgroup crawler \
    && adduser -g '' -H -D -G crawler crawler \
    && apk add --no-cache --virtual .run-deps \
    		bash \
    		ca-certificates \
    		coreutils \
    		curl \
    		grep \
    		jq \
    		openssl

COPY rootfs/ /
COPY crawl.sh /usr/local/bin/
COPY levenshtein.awk /usr/local/bin/

USER crawler
ENTRYPOINT ["/entrypoint.sh"]
