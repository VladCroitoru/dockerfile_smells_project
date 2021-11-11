FROM node:latest

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# These are intentionally separate so we don't have to re-install purescript when we change bower dependencies
COPY package.json /usr/src/app
RUN npm i

COPY bower.json /usr/src/app
RUN npm run-script bower -- --allow-root i

COPY . /usr/src/app

RUN npm run pulp build

ENTRYPOINT [ "/usr/src/app/docker-entrypoint.sh" ]
CMD [ "errybody" ]
