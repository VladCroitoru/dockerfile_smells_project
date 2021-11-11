FROM node:14.17.3-alpine

COPY . /app

WORKDIR /app

RUN npm install &&\
	npm install -g serve &&\
	npm run build

ENTRYPOINT ["serve", "-s", "build"]