FROM ubuntu:latest

WORKDIR /workspace

RUN apt-get update && \
	apt-get install -y make g++ python git curl && \
	curl -sL https://deb.nodesource.com/setup | sudo bash - && \
	apt-get install -y nodejs && \
	npm -g install node-gyp codebox && \
	cd /usr/lib/node_modules/codebox/node_modules/shux/node_modules/pty.js && \
	make clean && \
	make

EXPOSE 8000
ENTRYPOINT ["/usr/bin/codebox", "run"]