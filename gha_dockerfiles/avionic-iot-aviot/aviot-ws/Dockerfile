FROM node:14

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app
RUN npm install --production

COPY .babelrc /usr/src/app
COPY .eslintrc /usr/src/app
COPY .env.example /usr/src/app/

ENV NODE_ENV production
ENV MASTER_KEY "supersecret master key, PLEASE CHANGE"
ENV JWT_SECRET "jwt srcret, PLEASE CHANGE"

# populated by kubernetes
ENV REDIS_SERVICE_HOST ""
ENV REDIS_SERVICE_PORT ""
ENV MONGO_SERVICE_HOST ""
ENV MONGO_SERVICE_PORT ""

ENV PORT 8080
EXPOSE 8080



COPY src /usr/src/app/

CMD ["npm", "run", "prod"]
