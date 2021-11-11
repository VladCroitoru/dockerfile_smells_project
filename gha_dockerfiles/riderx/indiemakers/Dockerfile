FROM node:14-alpine

# Create app directory
WORKDIR /app
ADD . /app/

RUN yarn
RUN yarn build

ENV HOST 0.0.0.0
EXPOSE 3000

# start command
CMD [ "yarn", "start" ]
