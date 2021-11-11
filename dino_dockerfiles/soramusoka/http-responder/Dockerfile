FROM node:boron-alpine

# Create service directory
RUN mkdir -p /app
WORKDIR /app

# Bundle service source
COPY . /app

# Install service dependencies
COPY ./package.json ./yarn.lock /app/
RUN yarn && yarn run build

EXPOSE 3000
CMD ["yarn", "start"]
