FROM debian:jessie

ENV LC_ALL C
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
	curl && \
	curl -sL https://deb.nodesource.com/setup_iojs_1.x | bash -


RUN apt-get update && apt-get install -y \
	iojs \
	nginx

COPY nginx.conf /etc/nginx/

RUN mkdir /landing-page
WORKDIR /landing-page

COPY package.json ./
RUN npm install
COPY . .
RUN ./node_modules/gulp/bin/gulp.js

CMD ["nginx"]

EXPOSE 80
