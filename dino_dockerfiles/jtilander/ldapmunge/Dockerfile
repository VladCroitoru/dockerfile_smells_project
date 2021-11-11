FROM alpine:3.5

RUN apk add --no-cache \
		python \
		bash \
		curl


ENV VISUAL=vi
RUN mkdir /data && mkdir /app && mkdir /input
VOLUME ["/data", "/input"]

COPY docker-entrypoint.sh /
WORKDIR /app

COPY ldapmunge.py /app/

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["munge"]
