FROM node:14 AS ui-build

WORKDIR /usr/src/app
COPY readkit-web/ ./readkit-web/
RUN cd readkit-web && npm install @angular/cli && npm install && npm run build

FROM node:14-alpine AS server-build
WORKDIR /root/

RUN apk update \
	&& apk add --no-cache \
	autoconf \
	automake \
	file \
	build-base \
	nasm \
	musl \
	libpng-dev \
	zlib-dev \
	zip \
    unzip \
	python \
	python-dev \
	ruby \
	ruby-bundler \
	ruby-dev \
	ruby-rdoc \
	g++ \
	gcc \
	libxslt-dev \
	make \
	py-pip \
	git \
	&& rm -rf /var/lib/apk/*

RUN pip install lxml
RUN gem update --system && gem install compass --no-document
RUN npm install -g grunt

COPY --from=ui-build /usr/src/app/readkit-web/dist ./readkit-web/dist
COPY package*.json ./
COPY Gruntfile*.js ./
COPY readk.it ./readk.it/
COPY readkit.epub ./readkit.epub/


RUN npm install
COPY server.js .

EXPOSE 8080

RUN ls

CMD ["node", "server.js"]