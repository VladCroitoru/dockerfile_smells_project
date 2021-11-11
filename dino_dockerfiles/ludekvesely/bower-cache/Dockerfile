FROM alpine

RUN apk --update add nodejs git && \
	rm -rf /var/cache/apk/* /tmp/* && \
	npm install -g bower && \
	npm install -g npm-cache && \
	mkdir /app /cache

WORKDIR /app

ENTRYPOINT [ "npm-cache", "install", "--cacheDirectory", "/cache", "bower", "--allow-root" ]

