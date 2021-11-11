#BUILD
FROM node:slim as build
ENV NODE_ENV=production

WORKDIR /intranet-api
ENV PATH /intranet-api/node_modules/.bin:$PATH

COPY ./package.json ./
COPY ./package-lock.json ./
COPY ./run.sh ./

COPY . .

#PROD
FROM node:slim
WORKDIR /intranet-api

COPY --from=build intranet-api/run.sh /intranet-api/run.sh
COPY --from=build intranet-api/package.json /intranet-api/package.json
COPY --from=build intranet-api/api /intranet-api/api
COPY --from=build intranet-api/src /intranet-api/src

COPY . ./

RUN ["chmod", "+x", "./run.sh"]
CMD [ "./run.sh" ]
