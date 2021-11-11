FROM node:latest

RUN groupadd api-group
RUN useradd -ms /bin/bash api-user
WORKDIR /app
RUN chown -R api-user:api-group /app

USER api-user
COPY package.json /app/
RUN yarn install
COPY . /app/
COPY src/ /app/
CMD node index.js
EXPOSE 3000

