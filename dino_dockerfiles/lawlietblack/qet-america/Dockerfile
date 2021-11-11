FROM node:5.12

MAINTAINER Kenneth Black

COPY 		. /var/www
WORKDIR 	/var/www

RUN 		npm install

EXPOSE 3000

ENTRYPOINT ["node", "keystone"]
