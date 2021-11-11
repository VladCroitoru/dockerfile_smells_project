FROM node:6

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app

ENV npm_config_loglevel=warn

COPY package.json /usr/src/app/
RUN npm install

COPY typings.json /usr/src/app/
RUN npm run typings-install

COPY tsconfig.json /usr/src/app
COPY src /usr/src/app/src

ENV NODE_ENV=production
RUN npm run build

ENTRYPOINT ["npm", "run"]

# Default npm script (allow overriding to run tests, for example).
CMD ["start"]

EXPOSE 80
