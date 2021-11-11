FROM michbil/wrio:latest
MAINTAINER denso.ffff@gmail.com

COPY package.json /srv/package.json
RUN cd /srv/ && npm install #
COPY . /srv/www/

EXPOSE 5005
CMD cd /srv/www/ && rm -fr node_modules && nodemon index.js