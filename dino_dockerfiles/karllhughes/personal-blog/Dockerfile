# Prod Dockerfile
FROM node:8

# Create base directory
RUN mkdir /src
WORKDIR /src

# Install packages
COPY ./package.json /src/package.json
RUN npm install --silent

# Add code
COPY ./ /src

# Run webpack
RUN node node_modules/.bin/webpack

ENV NODE_ENV production

EXPOSE 3000

CMD ["node", "bin/www"]
