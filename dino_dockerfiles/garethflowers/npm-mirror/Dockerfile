FROM node:11.14.0-alpine

CMD [ "su-exec", "node", "verdaccio" ]
ENTRYPOINT [ "/opt/docker/entrypoint.sh" ]
EXPOSE 4873
HEALTHCHECK CMD netstat -ln | grep 4873 || exit 1
VOLUME [ "/var/opt/verdaccio" ]
WORKDIR /var/opt/verdaccio

RUN apk add --no-cache --virtual .build-deps \
	make \
	python \
	&& npm --global install verdaccio@3.11.6 \
	&& apk del .build-deps \
	&& apk add su-exec

COPY [ "src/entrypoint.sh", "/opt/docker/entrypoint.sh" ]
COPY [ "src/config.yaml", "/var/opt/verdaccio" ]
