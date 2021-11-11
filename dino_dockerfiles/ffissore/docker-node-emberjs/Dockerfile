FROM node:6

RUN usermod -u 500 node; \
    groupmod -g 500 node; \
    chown node:node -R /home/node

RUN npm install -g ember-cli
RUN npm install -g bower
RUN npm install -g phantomjs

# install watchman
RUN \
	git clone https://github.com/facebook/watchman.git &&\
	cd watchman &&\
	git checkout v3.9.0 &&\
	./autogen.sh &&\
	./configure --without-python &&\
	make -j &&\
	make install

RUN rm -rf /root/.npm

EXPOSE 4200
WORKDIR /app

