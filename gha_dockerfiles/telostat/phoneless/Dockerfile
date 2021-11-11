##################
## PHASE: BUILD ##
##################

FROM node:14.18 as build

WORKDIR /usr/src/app
COPY . .
RUN yarn install && yarn build

####################
## PHASE: RUNTIME ##
####################

FROM node:14.18

WORKDIR /app

COPY --from=build /usr/src/app/dist/index.js index.js

EXPOSE 3001

CMD [ "node", "--no-deprecation", "./index.js"]
