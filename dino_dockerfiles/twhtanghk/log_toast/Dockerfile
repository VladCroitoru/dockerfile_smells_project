FROM	node

WORKDIR /usr/src/app
ADD	https://github.com/twhtanghk/log_toast/archive/master.tar.gz /tmp
RUN	tar --strip-components=1 -xzf /tmp/master.tar.gz && \
	npm install && \
	node_modules/.bin/gulp
EXPOSE	8080

CMD npm test
