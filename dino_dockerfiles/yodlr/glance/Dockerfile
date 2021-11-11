FROM yodlr/nodejs

MAINTAINER Jared De La Cruz <jared@getyodlr.com>

# Install app
WORKDIR /src

ADD package.json /src/package.json
RUN npm install

ADD bower.json /src/bower.json
RUN bower install --allow-root

ADD gulpfile.js /src/gulpfile.js
RUN gulp

EXPOSE 3000

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

ADD . /src/

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
