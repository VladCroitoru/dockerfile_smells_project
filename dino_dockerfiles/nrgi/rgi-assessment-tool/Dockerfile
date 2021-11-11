FROM	node:6.14
MAINTAINER Chris Perry, cperry@resourcegovernance.org

RUN	npm install -g bower forever grunt

# Build src
COPY . /src
WORKDIR /src

RUN npm install && \
    npm cache clear
RUN	bower install --allow-root
RUN grunt build && grunt hash

EXPOSE  80

CMD     ["/src/node_modules/forever/bin/forever","/src/server.js"]
