FROM node:8-alpine
MAINTAINER Tommy Brunn <tommy.brunn@gmail.com>

WORKDIR /app
COPY yarn.lock /app
RUN yarn install
COPY . /app

# Yarn doesn't properly install global modules
RUN npm install -g .

ENTRYPOINT ["spring-config"]
CMD ["--help"]