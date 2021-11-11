FROM node:0.12-slim

ENV TINI_VERSION 0.6.0
RUN set -x \
	&& apt-get update && apt-get install -y ca-certificates curl \
		--no-install-recommends \
	&& rm -rf /var/lib/apt/lists/* \
	&& curl -fSL "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini" -o /usr/local/bin/tini \
	&& chmod +x /usr/local/bin/tini \
	&& tini -h \
	&& apt-get purge --auto-remove -y ca-certificates curl

ENV REDIS_COMMANDER 0.3.2

RUN npm install redis-commander@$REDIS_COMMANDER

WORKDIR /node_modules/redis-commander

ENV REDIS_PASS=""
ENV REDIS_DB=0
ENV REDIS_PORT=6379
ENV WEB_USER="user"
ENV WEB_PASS="pass"

COPY docker-entrypoint.sh ./
ENTRYPOINT ["./docker-entrypoint.sh"]

EXPOSE 8081
CMD ["tini", "--", "node", "bin/redis-commander.js"]
