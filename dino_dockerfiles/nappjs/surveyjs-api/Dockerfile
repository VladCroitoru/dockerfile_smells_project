FROM node:8.9.0-alpine

COPY . /code
WORKDIR /code

RUN rm -rf node_modules && yarn install --production --ignore-engines
CMD ["npm", "start"]