FROM	node:latest
MAINTAINER	Hardik 'neoXsys' Dalwadi hardik.dalwadi@gmail.com
ENV	NODE_ENV=production PORT=3000
ADD	. /var/www
WORKDIR	/var/www
RUN npm install
EXPOSE	$PORT
ENTRYPOINT	["npm","start"]
