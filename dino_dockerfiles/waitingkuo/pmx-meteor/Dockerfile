FROM google/nodejs

RUN apt-get install -y curl git gcc make build-essential imagemagick
RUN curl https://install.meteor.com | /bin/sh
RUN npm install --silent -g meteorite

ADD . ./meteorsrc
WORKDIR /meteorsrc
RUN mrt install && meteor bundle --directory /var/www/app

WORKDIR /var/www/app
RUN cd programs/server/node_modules &&  rm -rf fibers bcrypt
RUN npm install fibers@1.0.1 bcrypt@0.7.7

ENV PORT 80
EXPOSE 80

CMD node ./main.js
