FROM node:9.8.0

MAINTAINER cciccia

RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y netcat \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /src

RUN yarn global add nodemon sequelize-cli gulp

RUN chmod -R 777 .
ADD package.json package.json

RUN yarn

ENTRYPOINT ["yarn"]
CMD ["start"]

