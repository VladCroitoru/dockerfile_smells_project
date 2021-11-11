# BUILD: docker build -t josephg/boilerplate-lib .
# RUN: docker run -p 4433:4433 -v /db:/boilerplate-library/db josephg/boilerplate-lib 

FROM node

VOLUME /.npm
ENV NODE_ENV production

ADD . /boilerplate-library
WORKDIR /boilerplate-library
RUN npm install --production
RUN npm run-script prepublish

VOLUME /boilerplate-library/db

CMD ["/usr/local/bin/npm", "start"]
