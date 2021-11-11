FROM python:3-alpine
RUN apk add gcc musl-dev --no-cache \
	&& pip install streamlink \
	&& apk del gcc musl-dev --no-cache \
	&& rm -Rf /tmp/*
EXPOSE 8080
ENTRYPOINT ["streamlink", \
	"--player-external-http", \
	"--player-external-http-port", "8080" \
]
