FROM node:15.14.0 as build

LABEL stage=build

WORKDIR /usr/local/app

COPY ./ /usr/local/app/

RUN npm install --loglevel=error

RUN npm run build --loglevel=error

FROM node:15.14.0

RUN mkdir -p /usr/local/app/dist

COPY --from=build /usr/local/app/package.json /usr/local/app/package.json
COPY --from=build /usr/local/app/package-lock.json /usr/local/app/package-lock.json
COPY --from=build /usr/local/app/dist /usr/local/app/dist
COPY --from=build /usr/local/app/server.js /usr/local/app/server.js

WORKDIR /usr/local/app/

RUN npm install --loglevel=error

ENV PORT=80

EXPOSE 80

CMD ["node", "server.js"]