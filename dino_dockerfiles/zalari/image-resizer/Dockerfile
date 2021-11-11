FROM node:7

# https://github.com/yarnpkg/yarn/issues/2266
RUN yarn global add node-gyp

WORKDIR /srv/image-resizer-instance

RUN yarn global add https://github.com/zalari/image-resizer/ \
	&& image-resizer new \
	&& yarn install --production \
	&& yarn add ejs \
	&& yarn cache clean

RUN yarn global add pm2

ENTRYPOINT ["pm2-docker", "./server.js"]
