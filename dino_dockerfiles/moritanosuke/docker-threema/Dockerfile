FROM	node:7.5.0

ENV	THREEMA_VERSION=v1.1.0

RUN	git clone --branch ${THREEMA_VERSION} https://github.com/threema-ch/threema-web.git
# add local config
COPY	config.ts threema-web/src/config.ts
# build release tarball
RUN	cd threema-web && npm install

WORKDIR	threema-web
CMD	["npm", "run", "serve:live"]
