FROM node:6

# directory bootstrap
RUN mkdir -p /srv/app
WORKDIR /srv/app

# copy source
COPY index.js package.json npm-shrinkwrap.json /srv/app/
# build
RUN npm install

# run
CMD [ "npm", "start" ]
