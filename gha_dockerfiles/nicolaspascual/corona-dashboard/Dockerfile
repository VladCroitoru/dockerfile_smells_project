FROM node:12.16.0

WORKDIR /app
COPY yarn.lock package.json node_modules.* /app/
RUN yarn install

COPY . /app/

EXPOSE 3000