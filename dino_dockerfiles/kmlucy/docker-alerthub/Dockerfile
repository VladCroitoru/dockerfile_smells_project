FROM mhart/alpine-node:8
LABEL maintainer "Kyle Lucy <kmlucy@gmail.com>"

WORKDIR /app
RUN apk --no-cache add git && \
	cd /app && \
	git clone https://github.com/Ardakilic/alerthub.git /app && \
	npm install && \
	apk del git

CMD ["npm", "start"]
