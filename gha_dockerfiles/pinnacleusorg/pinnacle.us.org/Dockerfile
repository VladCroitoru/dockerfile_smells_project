FROM node:15 as builder

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install
COPY . .

RUN npm run build

FROM builder as staging
ENV PORT=9000
ENV NODE_ENV="development"
ENV API_ROOT="https://api-staging.pinnacle.us.org/1.0"
ENV LOCAL_ROOT="https://staging.pinnacle.us.org"
EXPOSE 9000
CMD ["node", "__sapper__/build"]

FROM builder as production
ENV PORT=9001
ENV NODE_ENV="production"
ENV API_ROOT="https://api.pinnacle.us.org/1.0"
ENV LOCAL_ROOT="https://pinnacle.us.org"
EXPOSE 9001
CMD ["node", "__sapper__/build"]
