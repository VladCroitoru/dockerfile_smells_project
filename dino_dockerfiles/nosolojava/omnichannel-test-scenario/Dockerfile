# start from nosolojava apache-node-docker
FROM nosolojava/apache-node-docker


# first download npm dependencies
ADD package.json /tmp/package.json
WORKDIR /tmp
RUN npm install
RUN mkdir -p /opt/app && cp -a /tmp/node_modules /opt/app/


# Bundle app source
COPY .bowerrc /opt/app/.bowerrc
COPY .buildignore /opt/app/.buildignore
COPY  bower.json /opt/app/bower.json
COPY  Gruntfile.js /opt/app/Gruntfile.js
COPY  karma.conf.js /opt/app/karma.conf.js
COPY  package.json /opt/app/package.json
COPY  protractor.conf.js /opt/app/protractor.conf.js
COPY  client /opt/app/client



WORKDIR /opt/app

RUN npm install 
RUN bower install
RUN grunt

RUN cp -a /opt/app/dist/public/* /app/


# the static content is mapped in the docker-compose.yml
#   volumes:
#   - ./vhosts:/bitnami/apache/conf/vhosts
#   - ./dist/public:/app
