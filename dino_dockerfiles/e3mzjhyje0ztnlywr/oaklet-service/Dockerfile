FROM java:openjdk-7u91-jre-alpine

ADD package.zip.enc /home

RUN apk update && \
	apk add openssl unzip bash

CMD cd /home && \
	openssl enc -d -aes-256-cbc -in package.zip.enc -out package.zip -pass pass:$UNLOCK_KEY && \
	unzip package.zip && \
	mv package/* . && \
	bin/oaklet