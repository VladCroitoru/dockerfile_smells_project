# set up
FROM node:alpine as env
ENV HOST 0.0.0.0
EXPOSE 3001

# restore
FROM env as restore
WORKDIR /src
Copy ./package.json .
RUN yarn install \
  --prefer-offline \
  --pure-lockfile \
  --non-interactive \
  --production=false

# build
FROM restore as build
WORKDIR /src
COPY . .
RUN yarn build

# run
FROM build as final
WORKDIR /src/dist
CMD [ "node", "index.js" ]
