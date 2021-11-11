FROM node:8.16.0-alpine
MAINTAINER Michael Prinsloo <github.com/prinsmike>

RUN apk add --no-cache --virtual .persistent-deps \
	curl \
	openssl \
	git \
	openssh \
	make \
	gcc \
	g++ \
	python \
	py-pip && \
	npm install --silent --save-dev -g \
		gulp-cli \
		typescript \
		webpack \
		create-react-app

# Set up the application directory.
VOLUME ["/app"]
WORKDIR /app

CMD ["npm", "-v"]
