#
# Builder stage.
# This state compile our TypeScript to get the JavaScript code
#
FROM node:12.13.0 AS builder

WORKDIR /usr/src/app

COPY package*.json ./
COPY tsconfig*.json ./
COPY ./src ./src
RUN npm ci --quiet && npm run build

FROM node:latest as build

# Production stage.
# This state compile get back the JavaScript code from builder stage
# It will also install the production package only
#
FROM node:12.13.0-alpine

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

WORKDIR /app
ENV NODE_ENV=production

COPY package*.json ./
RUN npm ci --quiet --only=production

## We just need the build to execute the command
COPY --from=builder /usr/src/app/dist ./dist

# COPY .env .
COPY config .

EXPOSE 8080

CMD ["node", "dist/server.js" ]

#RUN mkdir /app
#WORKDIR /app
#
#ARG NODE_ENV=production
#
#ENV PATH /app/node_modules/.bin:$PATH
#ENV NODE_ENV=${NODE_ENV}
#
#COPY package.json package-lock.json /app/
#
#RUN npm install
#
#COPY . /app/
#
#RUN npm run build
#
#EXPOSE 8080
#
#CMD ["node", "dist/server.js" ]
